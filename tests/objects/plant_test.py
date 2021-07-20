import pytest
from ceaos.objects.plants import Plant


def setup_plant() -> Plant:
    return Plant("test_plant")


def test_creation():
    Plant("test_plant")


def test_get_name():
    p = setup_plant()
    assert (p.name == "test_plant")


def test_set_name():
    p = setup_plant()
    p.set_name(123)
    assert (type(p.name) == str)


def test_add_property():
    p = setup_plant()
    p = Plant("test_plant")
    p.add_property("age", 1)
    assert (p.properties.get("age") == 1 and len(p.properties) == 1)


def test_delete_property():
    p = setup_plant()
    p.add_property("age", 1)
    p.delete_property("age")
    assert (len(p.properties) == 0)
