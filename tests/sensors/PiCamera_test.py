import pytest
from ceaos.sensors.PiCamera import PiCam


def setup_sensor() -> PiCam:
    return PiCam()


def test_creation():
    PiCam()


def test_value_exception():
    a = setup_sensor()
    with pytest.raises(ValueError):
        a.set_file_path(False)
