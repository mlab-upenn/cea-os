from ceaos.objects.beds import Bed
from ceaos.objects.environment import Environment
from ceaos.objects.farm import Farm
from ceaos.sensors.artificial_sensor import Artificial_Sensor
from ceaos.actuators import Artificial_Actuator
import pytest
from ceaos.api.parser import parse, get_available_endpoints, find_target
from ceaos.api import create_api


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
        return "SUCCESS"


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


def test_full_api_flow():
    import zmq
    import json
    import threading

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
    api = threading.Thread(target=create_api, args=(f,), daemon=True)
    api.start()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:23267")
    socket.send_string(message)
    reply = socket.recv()
    reply = json.loads(reply)

    assert reply['status'] == 200 and reply['response'] == 'SUCCESS'
    assert endp._endpoint_hit
    assert endp._payload_val == {"new_val": "NV", "other_val": 132}
