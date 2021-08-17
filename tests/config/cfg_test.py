import pytest
from ceaos.cfg import check_name, check_sensors, add_sensors, load_config
from ceaos.actuators.network_actuator import NetworkActuator
from ceaos.objects.environment import Environment


def test_config1():
    farm, sensors, connection, error = load_config("tests.config", "test_config1.yaml")
    error_location = "test_farm"
    assert (
        error
        == 'ERROR: Must have "environments" list in farm' + "(%s)" % error_location
    )

def test_check_name():
    test_dict1 = {"n": "Kevin"}
    test_dict2 = {"name": None}
    t1 = check_name(test_dict1)
    t2 = check_name(test_dict2)
    assert (t1, t2) == (False, False)


def test_check_sensors():
    test_dict1 = {
        "name": "test_farm",
        "sensors": [{"value": 25}],
    }  # Does not contain "type" field
    test_dict2 = {"name": "test_farm2"}
    t1 = check_sensors(test_dict1)
    t2 = check_sensors(test_dict2)
    assert (t1, t2) == (False, True)


def test_add_sensors():
    test_env = Environment("env1")
    sensors_list = []
    test_dict = {
        "name": "env1",
        "sensors": [
            {"type": "temp", "value": 10},
            {"type": "pH", "value": 5.8},
            {"type": "EC", "value": 0.8},
        ],
    }
    location = ["farm1", "env1"]
    add_sensors(test_env, test_dict, sensors_list, location)
    assert len(sensors_list) == 3
