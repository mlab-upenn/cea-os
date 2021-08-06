import pytest
from ceaos.grow import load_grow


def test_grow1():
    tocompare = dict()
    recipe_list = load_grow("tests.config", "test_grow.yaml")
    recipe1 = {
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
    recipe2 = {
        'name':
        'growing',
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
            'min': 10,
            'unit': 'hours'
        },
        'DLI': {
            'max': 14,
            'min': 12,
            'unit': 'mol*m-2*d-1'
        },
        'pH': {
            'max': 6.2,
            'min': 5.6,
            'unit': 'pH'
        },
        'EC': {
            'max': 1.2,
            'min': 0.8,
            'unit': 'S/m'
        }
    }
    tocompare["stage1"] = recipe1
    tocompare["stage2"] = recipe2
    assert (tocompare == recipe_list)
