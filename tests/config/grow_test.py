import pytest
from ceaos.grow import load_grow, configure_autogrowers
from ceaos.actuators.network_actuator import NetworkActuator
from ceaos.sensors.nwsensor import NetworkSensor
from ceaos.autogrowers.pump_grower import PumpGrower

def test_autgrowers():
    autogrowers = dict()
    sensors = []
    actuators = []
    sen = NetworkSensor()
    sen.datatype = "reservoir"
    act = NetworkActuator("198.168.1.126", "26462")
    act.datatype = "EC"
    act.refresh_rate = 5
    sensors.append(sen)
    actuators.append(act)
    g1 = PumpGrower("eca")
    g2 = PumpGrower("ecb")
    g1.refresh_rate = act.refresh_rate
    g2.refresh_rate = act.refresh_rate
    g1.add_inputs("sensor", sen)
    g1.add_inputs("actuator", act)
    g2.add_inputs("sensor", sen)
    g2.add_inputs("actuator", act)
    if g1.refresh_rate not in autogrowers:
        autogrowers[g1.refresh_rate] = [g1]
        autogrowers.get(g1.refresh_rate).append(g2)
    else:
        autogrowers.get(g1.refresh_rate).append(g1)
        autogrowers.get(g1.refresh_rate).append(g2)
    ag = configure_autogrowers(sensors, actuators)
    assert (g1.name == ag[5][0].name)

def test_grow1():
    tocompare = dict()
    recipe_list = load_grow("test_grow.yaml", "tests.config")
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
