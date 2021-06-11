import pytest
from ceaos.sensors.sensor_definition import Sensor


def test_creation():
    with pytest.raises(NotImplementedError):
        Sensor()
