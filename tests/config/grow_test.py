import pytest
from ceaos.grow import load_grow, parse_recipe, find_relevantbeds
from ceaos.objects.beds import Bed
from ceaos.objects.farm import Farm


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
    bed_names = []
    bed_names.append("bed1")
    bed_names.append("bed2")
    bed_list = dict()
    bed1 = Bed("bed1")
    bed2 = Bed("bed2")
    bed_list["bed1"] = bed1
    bed_list["bed2"] = bed2
    compare = []
    compare.append(bed1)
    compare.append(bed2)
    relevant = find_relevantbeds(bed_names, bed_list)
    assert (relevant == compare)
