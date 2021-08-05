import yaml
from datetime import datetime, time
from .objects.farm import Farm
from .objects.beds import Bed
from .objects.environment import Environment
from .actuators.sample_actuator import Artificial_Actuator
from importlib_resources import files


def get_relevant_beds(farm, env_list, bed_names_list):
    all_beds = dict()
    environments = farm.get_envs()
    for environment in environments:
        if environment in env_list:
            beds = environments[environment].get_beds()
            for bed in beds:
                if bed in bed_names_list:
                    all_beds[bed] = beds[bed]

    return all_beds


def send_command(actuator_list, max, min, actuation):
    for actuator in actuator_list:
        actuator.set_point(min, max)


# needs work
def day_or_night(recipe):
    # this time stuff is not accurate, more of a placeholder
    for timeperiod in recipe["air_temperature"]:
        if datetime.utcnow().time() < time(
                20, 0) and datetime.utcnow().time() > time(6, 0):
            period = timeperiod
        else:
            period = timeperiod

    return period

def find_actuators(bed_list, k):
    actuators = []
    for bed in bed_list:
        bed_actuators = bed.get_actuators()
        for actuator in bed_actuators:
            if k in actuator:
                actuators.append(bed_actuators[actuator])

    return actuators


def parse_recipe(recipe, bed_list):
    for k in recipe:
        if k == 'air_temperature':
            period = day_or_night(recipe)
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, period["max"], period["min"],
                         "air_temperature")
        elif k == 'water_temperature':
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'],
                         "water_temperature")
        elif k == 'relative_humidity':
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'],
                         "relative humidity")
        elif k == 'light_hours':
            acuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'],
                         "light_hours")
        elif k == 'DLI':
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'], "DLI")
        elif k == 'pH':
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'], "pH")
        elif k == 'EC':
            actuator_list = find_actuators(bed_list, k)
            send_command(actuator_list, recipe[k]['max'], recipe[k]['min'], "EC")
        elif k == 'name':
            name = recipe['name']

    return name


def load_grow(farm,
              config_folder="ceaos.resources.config",
              config_file="config_lettuce_grow.yml"):
    config = files(config_folder).joinpath(config_file).read_text()
    try:
        dictionary = yaml.safe_load(config)
    except yaml.YAMLError as e:
        print(e)
        quit()

    bed_names_list = []

    env_list = []

    for envs in dictionary.get("environments"):
        env_list.append(envs['name'])

    for beds in dictionary.get("beds"):
        bed_names_list.append(beds['name'])

    bed_list = get_relevant_beds(farm, env_list, bed_names_list)

    for stage in dictionary.get("stage_ordering"):
        for stages in stage:
            if stage.get('order') == 1:
                stage1 = stage.get('name')
            elif stage.get('order') == 2:
                stage2 = stage.get('name')
            else:
                stage3 = stage.get('name')

    recipe_list = []
    for stages in dictionary.get('stages'):
        if stages.get('name') == stage1:
            recipe1 = stages
            recipe_list.append(recipe1)
        elif stages.get('name') == stage2:
            recipe2 = stages
            recipe_list.append(recipe2)
        else:
            recipe3 = stages
            recipe_list.append(recipe3)

    for recipe in recipe_list:
        if recipe == recipe1:
            parse_recipe(recipe, bed_list)

    return recipe_list
