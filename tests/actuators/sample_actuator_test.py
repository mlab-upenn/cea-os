import pytest
from ceaos.actuators.sample_actuator import ArtificialActuator
from ceaos.sensors.artificial_sensor import ArtificialSensor


def setup_actuator() -> ArtificialActuator:
    return ArtificialActuator()


def test_creation():
    ArtificialActuator()


def test_read():
    a = setup_actuator()
    with pytest.raises(NotImplementedError):
        a.setpoint()


def test_value_exception():
    a = setup_actuator()
    with pytest.raises(ValueError):
        a.set_noise("A")
