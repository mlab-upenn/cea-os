import pytest
from ceaos.autogrowers.autogrower_definition import Auto_Grower


def test_creation():
    with pytest.raises(NotImplementedError):
        Auto_Grower()