import pytest
from ceaos.actuators.sample_actuator import Artificial_Actuator
from ceaos.sensors.artificial_sensor import Artificial_Sensor


def setup_actuator() -> Artificial_Actuator:
    return Artificial_Actuator()


def test_creation():
    Artificial_Actuator()


def test_read():
    a = setup_actuator()
    with pytest.raises(NotImplementedError):
        a.set_point()


def test_stop():
    a = setup_actuator()
    a.stop()
    assert (a.running is False)


def test_value_exception():
    a = setup_actuator()
    with pytest.raises(ValueError):
        a.set_noise("A")
