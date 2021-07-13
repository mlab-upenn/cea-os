import pytest
from ceaos.objects.farm import Farm
from ceaos.objects.environment import Environment


def setup_farm() -> Farm:
    return Farm("test_farm")


def test_creation():
    Farm("test_farm")


def test_get_name():
    f = setup_farm()
    assert (f.get_name() == "test_farm")


def test_set_name():
    f = setup_farm()
    f.set_name(2)
    assert (type(f.get_name()) == str)


def test_add_env():
    f = setup_farm()
    env = Environment("env1")
    f.add_environment(env)
    assert (f.num_environments == 1)
