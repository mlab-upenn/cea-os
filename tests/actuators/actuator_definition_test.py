import pytest
from ceaos.actuators.actuator_definition import Actuator


def test_creation():
    with pytest.raises(NotImplementedError):
        Actuator()
