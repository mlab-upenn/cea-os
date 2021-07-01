from ceaos.objects.beds import Bed
from ceaos.objects.environment import Environment
from ceaos.objects.farm import Farm
from ceaos.sensors.artificial_sensor import Artificial_Sensor
from ceaos.actuators import Artificial_Actuator
import pytest
from ceaos.api.parser import parse, get_available_endpoints, find_target


class FakeEndpoint:
    def __init__(self):
        self._endpoint_hit = False
        self._payload_val = None

    def endpoint(self, new_val):
        self._endpoint_hit = True
        self._payload_val = new_val

    def val_getter(self):
        return self._payload_val

    def multi_arg(self, new_val, other_val):
        self._endpoint_hit = True
        self._payload_val = {"new_val": new_val, "other_val": other_val}


def setup_farm_one() -> Farm:
    f = Farm("f1")
    env0 = Environment("env0")
    env0.add_sensor("temp", Artificial_Sensor())
    f.add_environment(env0)
    env1 = Environment("env1")
    bed0 = Bed("bed0")
    bed0.add_actuators("air_conditioner", Artificial_Actuator())
    bed0.add_sensor("test_sensor", FakeEndpoint())
    env1.add_bed(bed0)
    f.add_environment(env1)
    return f


def test_parser_objects():
    f = setup_farm_one()
    assert find_target("f1.env0", f) == f.environments["env0"]
    assert find_target("f1.env0.temp", f) == f.environments["env0"].sensors["temp"]
    assert (
        find_target("f1.env1.bed0.air_conditioner", f)
        == f.environments["env1"].beds["bed0"].actuators["air_conditioner"]
    )


def test_errors():
    f = setup_farm_one()
    with pytest.raises(ValueError):
        find_target("farm.env0", f)

    with pytest.raises(ValueError):
        find_target("farm.env0.temp.read_value", f)


def test_parse_setter():
    import json

    f = setup_farm_one()
    endp = f.environments["env1"].beds["bed0"].sensors["test_sensor"]
    assert not endp._endpoint_hit
    assert endp._payload_val is None
    message = json.dumps(
        {
            "cea-addr": "f1.env1.bed0.test_sensor",
            "action": "endpoint",
            "payload": "SUCCESS",
        }
    )
    parse(message, f)  # No return expected
    assert endp._endpoint_hit
    assert endp._payload_val == "SUCCESS"


def test_parse_payload_error():
    import json

    f = setup_farm_one()
    endp = f.environments["env1"].beds["bed0"].sensors["test_sensor"]
    endp._payload_value = 100
    message = json.dumps(
        {
            "cea-addr": "f1.env1.bed0.test_sensor",
            "action": "val_getter",
            "payload": "SUCCESS",
        }
    )
    with pytest.raises(TypeError):
        parse(message, f)  # We expect an error here


def test_parse_return_values():
    import json

    f = setup_farm_one()
    endp = f.environments["env1"].beds["bed0"].sensors["test_sensor"]
    endp._payload_val = 100
    message = json.dumps(
        {"cea-addr": "f1.env1.bed0.test_sensor", "action": "val_getter"}
    )
    retval = parse(message, f)
    assert retval == 100


def test_parse_dict_data():
    import json

    f = setup_farm_one()
    endp = f.environments["env1"].beds["bed0"].sensors["test_sensor"]
    endp._payload_val = 100
    message = json.dumps(
        {
            "cea-addr": "f1.env1.bed0.test_sensor",
            "action": "multi_arg",
            "payload": {"new_val": "NV", "other_val": 132},
        }
    )
    parse(message, f)
    assert endp._endpoint_hit
    assert endp._payload_val == {"new_val": "NV", "other_val": 132}
