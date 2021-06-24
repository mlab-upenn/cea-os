import pytest
from ceaos.sensors.artificial_camera import Artificial_Camera


def setup_sensor() -> Artificial_Camera:
    return Artificial_Camera()


def test_creation():
    Artificial_Camera()


def test_read():
    a = setup_sensor()
    assert (type(a.read_value()) == str)


def test_value_exception():
    a = setup_sensor()
    with pytest.raises(FileNotFoundError):
        a.set_image("A_nonexistent_file.jpg")


def test_value_set():
    a = setup_sensor()
    a.set_image("a_plant.jpg")
    a.set_value()
    f = open("a_plant.jpg", "rb")  # open original image
    raw_image = f.read()
    assert (a.decode_value() == raw_image)  # compare decoded image to original
