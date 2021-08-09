import pytest
from ceaos.objects.plants import Plant
from ceaos.objects.beds import Bed
from ceaos.sensors.artificial_sensor import Artificial_Sensor


def setup_bed() -> Bed:
    return Bed("test_bed")


def test_creation():
    Bed("test_bed")


def test_get_name():
    b = setup_bed()
    assert (b.name == "test_bed")


def test_set_name():
    b = setup_bed()
    b.set_name(123)
    assert (type(b.name) == str)


def test_add_plant():
    b = setup_bed()
    p = Plant("test_plant")
    b.add_plant(p)
    assert (len(b.plants) == 1 and len(b.plants.keys()) == 1)


def test_add_sensor():
    b = setup_bed()
    s = Artificial_Sensor()
    b.add_sensor("test_sens", s)
    assert (len(b.sensors) == 1 and len(b.sensors.keys()) == 1)


def test_delete_plant():
    b = setup_bed()
    p = Plant("test_plant")
    b.add_plant(p)
    b.delete_plant(p)
    assert (len(b.plants) == 0 and len(b.plants.keys()) == 0)
