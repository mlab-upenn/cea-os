import pytest
from ceaos.sensors.artificial_sensor import Artificial_Sensor


def setup_sensor() -> ArtificialSensor:
    return Artificial_Sensor()


def test_creation():
    Artificial_Sensor()


def test_none_value():
    with pytest.raises(TypeError):
        Artificial_Sensor(value=None)


def test_read():
    a = setup_sensor()
    assert type(a.read_value()) == float


def test_value_set():
    a = setup_sensor()
    a.set_value(25.0)
    assert a.value == 25.0


def test_value_exception():
    a = setup_sensor()
    with pytest.raises(ValueError):
        a.set_value("A")
