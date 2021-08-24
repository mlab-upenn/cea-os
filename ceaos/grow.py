import yaml
from .autogrowers.pump_grower import PumpGrower
from .autogrowers.time_grower import TimeGrower
import time
from importlib_resources import files

def execute(refresh_rate, ag_list, recipe_list):
    for recipe in recipe_list:
        stage1 = recipe['stage1']
        hours = stage1["light_hours"]
        on = hours['max']
        off = 24 - hours['max']
    while True:
        for grower in ag_list:
            if type(grower) is TimeGrower:
                grower.control()
                time.sleep(refresh_rate)

# method configures inputs and outputs for various autogrowers
# depending on what kind of sensor, actuator pairings are 
# present in the config file. 
def configure_autogrowers(sensors, actuators):
    autogrowers = dict()
    for sensor in sensors:
        for actuator in actuators:
            if sensor.location == actuator.location:
                if sensor.datatype.lower() == "reservoir" and (actuator.datatype.lower() == "ec" or actuator.datatype.lower() == "ph"):
                    if actuator.datatype.lower() == "ec":
                        g1 = PumpGrower("ec")
                    elif actuator.datatype.lower() == "ph":
                        g1 = PumpGrower("ph")
                    g1.refresh_rate = actuator.refresh_rate
                    g1.add_inputs("sensor", sensor)
                    g1.add_inputs("value", 4)
                    g1.add_outputs("actuator", actuator)
                    if g1.refresh_rate not in autogrowers:
                        autogrowers[g1.refresh_rate] = [g1]
                    else:
                        autogrowers.get(g1.refresh_rate).append(g1)
                elif sensor.datatype.lower() == actuator.datatype.lower():
                    g2 = TimeGrower(sensor.name)
                    g2.refresh_rate = actuator.refresh_rate
                    g2.add_inputs("sensor", sensor)
                    g2.add_outputs("actuator", actuator)
                    if g2.refresh_rate not in autogrowers:
                        autogrowers[g2.refresh_rate] = [g2]
                    else:
                        autogrowers.get(g2.refresh_rate).append(g2)

    return autogrowers

def load_grow(config_file="config_lettuce_grow.yml", config_folder="ceaos.resources.config.recipes"):
    config = files(config_folder).joinpath(config_file).read_text()
    try:
        dictionary = yaml.safe_load(config)
    except yaml.YAMLError as e:
        print(e)
        quit()

    for stage in dictionary.get("stage_ordering"):
        for stages in stage:
            if stage.get('order') == 1:
                stage1 = stage.get('name')
            elif stage.get('order') == 2:
                stage2 = stage.get('name')
            else:
                stage3 = stage.get('name')

    recipe_stages = dict()
    for stages in dictionary.get('stages'):
        if stages.get('name') == stage1:
            recipe1 = stages
            recipe_stages["stage1"] = recipe1
        elif stages.get('name') == stage2:
            recipe2 = stages
            recipe_stages["stage2"] = recipe2
        else:
            recipe3 = stages
            recipe_stages["stage3"] = recipe3

    return recipe_stages

if __name__ == "__main__":
    load_grow()
