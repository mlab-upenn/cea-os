from ceaos.actuators.actuator_commands import set_airtemp
import yaml
import zmq
from datetime import datetime, time
from .objects.farm import Farm
from .objects.beds import Bed
from .objects.environment import Environment
from .actuators import actuator_commands
from importlib_resources import files
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def get_allbeds(farm):
    logging.info("I was here1")
    all_beds = dict()
    environments = farm.get_envs()
    for environment in environments:
        beds = environments[environment].get_beds()
        for bed in beds:
            all_beds[beds[bed].get_name()] = beds[bed]
    
    return all_beds

def find_relevantbeds(bed_names_list, all_beds):
    logging.info("I was here2")
    bed_list = []
    for names in bed_names_list:
        for names2 in all_beds:
            if names == names2:
                bed_list.append(all_beds[names2])

    return bed_list

def find_ips(bed_list, actuator):
    logging.info("I was here3")
    ip_list = []
    for bed in bed_list:
        for act in bed.get_actuators():
            if actuator in bed.get_actuators()[act]:
                ip_list.append(act)
    
    return ip_list

def send_command(ip_list, max, min, actuation):
    logging.info("I was here4")
    for ip in ip_list:
        if actuation == "air_temperature":
            actuator_commands.set_airtemp(ip, max, min)
        elif actuation == "water_temperature":
            print("no control over water temp")
        elif actuation == "relative_humidity":
            print("no control over relative humidity")
        elif actuation == "light_hours":
            actuator_commands.set_lights(ip, max, min)
        elif actuation == "pH":
            actuator_commands.set_pH(ip, max, min)
        elif actuation == "EC":
            actuator_commands.set_EC(ip, max, min)    


def load_grow(farm, config_folder="ceaos.resources.config", config_file="config_lettuce_grow.yml"):
    logging.info("I was here")
    config = files(config_folder).joinpath(config_file).read_text()
    try:
        dictionary = yaml.safe_load(config)
    except yaml.YAMLError as e:
        print(e)
        quit()
    
    bed_names_list = []

    for beds in dictionary.get("beds"):
        bed_names_list.append(beds['name'])
    
    all_beds = get_allbeds(farm)

    bed_list = find_relevantbeds(bed_names_list, all_beds)

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
        
    
    for k in recipe1:
        if k == 'air_temperature':
            #this time stuff is not accurate, more of a placeholder
            for timeperiod in recipe1["air_temperature"]:
                #if datetime.utcnow().time() < time(20, 0) and datetime.utcnow().time() > time(6, 0):
                if timeperiod["time_period"] == "day":
                    period = timeperiod
                else:
                    period = timeperiod

            ip_list = find_ips(bed_list, k)
            send_command(ip_list, period["max"], period["min"], "air_temperature")
        elif k == 'water_temperature':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "water_temperature")
        elif k == 'relative_humidity':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "relative humidity")
        elif k == 'light_hours':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "light_hours")
        elif k == 'DLI':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "DLI")
        elif k == 'pH':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "pH")
        elif k == 'EC':
            ip_list = find_ips(bed_list, k)
            send_command(ip_list, recipe1[k]['max'], recipe1[k]['min'], "EC")
        
        return recipe_list
        
