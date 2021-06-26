import pytest
from ceaos.sensors.artificial_camera import ArtificialCamera


def setup_sensor() -> ArtificialCamera:
    return ArtificialCamera()


def test_creation():
    ArtificialCamera()


def test_read():
    a = setup_sensor()
    assert (type(a.read_value()) == str)


def test_value_exception():
    a = setup_sensor()
    with pytest.raises(FileNotFoundError):
        a.set_image("tests/sensors/A_nonexistent_file.jpg")


def test_value_set():
    a = setup_sensor()
    a.set_image("tests/sensors/a_plant.jpg")
    a.set_value()
    f = open("tests/sensors/a_plant.jpg", "rb")  # open original image
    raw_image = f.read()
    assert (a.decode_value() == raw_image)  # compare decoded image to original
