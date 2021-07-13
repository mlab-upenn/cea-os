import pytest
from ceaos.objects.environment import Environment
from ceaos.objects.beds import Bed
from ceaos.sensors.artificial_sensor import Artificial_Sensor


def setup_env() -> Environment:
    return Environment("test_env")


def test_creation():
    Environment("test_farm")


def test_get_name():
    e = setup_env()
    assert (e.get_name() == "test_env")


def test_set_name():
    e = setup_env()
    e.set_name(123)
    assert (type(e.get_name()) == str)


def test_add_bed():
    e = setup_env()
    b = Bed("test_bed")
    e.add_bed(b)
    assert (e.num_beds == 1 and len(e.beds.keys()) == 1)


def test_add_sensor():
    e = setup_env()
    s = Artificial_Sensor()
    e.add_sensor("test_sens", s)
    assert (e.num_sensors == 1 and len(e.sensors.keys()) == 1)


def test_delete_bed():
    e = setup_env()
    b = Bed("test_bed")
    e.add_bed(b)
    e.delete_bed(b)
    assert (e.num_beds == 0 and len(e.beds.keys()) == 0)
