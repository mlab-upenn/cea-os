from ceaos import actuators
from ceaos.objects.environment import Environment
import pytest
from ceaos.grow import find_actuators, get_relevant_beds, load_grow, parse_recipe
from ceaos.objects.beds import Bed
from ceaos.objects.farm import Farm
from ceaos.actuators.sample_actuator import Artificial_Actuator


def test_grow1():
    farm = Farm("farm1")
    recipe_list = load_grow(farm, "tests.config", "test_grow.yaml")
    recipe = {
        'name':
        'seedling',
        'air_temperature': [{
            'time_period': 'day',
            'max': 75,
            'min': 68,
            'unit': 'F'
        }, {
            'time_period': 'night',
            'max': 55,
            'min': 55,
            'unit': 'F'
        }],
        'water_temperature': {
            'max': 75,
            'min': 65,
            'unit': 'F'
        },
        'relative_humidity': {
            'max': 70,
            'min': 50,
            'unit': '%'
        },
        'light_hours': {
            'max': 14,
            'min': 12,
            'unit': 'hours'
        },
        'DLI': {
            'max': 14,
            'min': 12,
            'unit': 'mol*m-2*d-1'
        },
        'pH': {
            'max': 6.5,
            'min': 5.5,
            'unit': 'pH'
        },
        'EC': {
            'max': 1.2,
            'min': 0.8,
            'unit': 'S/m'
        }
    }
    assert (recipe == recipe_list[0])


def test_parse_recipe():
    bed_list = []
    bed1 = Bed("bed1")
    bed2 = Bed("bed2")
    bed_list.append(bed1)
    bed_list.append(bed2)
    recipe = {
        'name':
        'seedling',
        'air_temperature': [{
            'time_period': 'day',
            'max': 75,
            'min': 68,
            'unit': 'F'
        }, {
            'time_period': 'night',
            'max': 55,
            'min': 55,
            'unit': 'F'
        }],
        'water_temperature': {
            'max': 75,
            'min': 65,
            'unit': 'F'
        },
        'relative_humidity': {
            'max': 70,
            'min': 50,
            'unit': '%'
        },
        'light_hours': {
            'max': 14,
            'min': 12,
            'unit': 'hours'
        },
        'DLI': {
            'max': 14,
            'min': 12,
            'unit': 'mol*m-2*d-1'
        },
        'pH': {
            'max': 6.5,
            'min': 5.5,
            'unit': 'pH'
        },
        'EC': {
            'max': 1.2,
            'min': 0.8,
            'unit': 'S/m'
        }
    }
    name = parse_recipe(recipe, bed_list)
    assert (name == "seedling")


def test_find_beds():
    env_list = []
    farm1 = Farm("farm1")
    env1 = Environment("env1")
    env_list.append(env1.name)
    farm1.add_environment(env1)
    bed_names = []
    bed_names.append("bed1")
    bed1 = Bed("bed1")
    bed2 = Bed("bed2")
    env1.add_bed(bed1)
    env1.add_bed(bed2)
    compare = dict()
    compare[bed1.name] = bed1
    relevant = get_relevant_beds(farm1, env_list, bed_names)
    assert (relevant == compare)

def test_find_actuators():
    bed_list = []
    bed1 = Bed("bed1")
    bed2 = Bed("bed2")
    ec = Artificial_Actuator()
    pH = Artificial_Actuator()
    water = Artificial_Actuator()
    bed1.add_actuators("Artificial EC", ec)
    bed1.add_actuators("Artificial pH", pH)
    bed2.add_actuators("Artificial water_temperature", water)
    bed_list.append(bed1)
    bed_list.append(bed2)
    actuators = []
    actuators.append(ec)
    relevant = find_actuators(bed_list, "EC")
    assert (actuators == relevant)


