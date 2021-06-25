from ceaos.objects.beds import Bed
from ceaos.objects.environment import Environment
from ceaos.objects.farm import Farm
from ceaos.sensors.artificial_sensor import Artificial_Sensor
from ceaos.actuators.actuator_definition import Actuator
import pytest
from ceaos.api.parser import parse, get_available_endpoints, find_target


def setup_farm_one() -> Farm:
    f = Farm("f1")
    env0 = Environment('env0')
    env0.add_sensor("temp",Artificial_Sensor())
    f.add_environment(env0)
    env1 = Environment('env1')
    bed0 = Bed("bed0")
    bed0.add_actuators("pump",)
    env1.add_bed(bed0)
    f.add_environment(env1)

