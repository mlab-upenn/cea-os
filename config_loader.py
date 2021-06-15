import yaml
from ceaos.objects.farm import Farm
from ceaos.objects.beds import Bed
from ceaos.objects.environment import Environment
from ceaos.objects.plants import Plant
from ceaos.sensors.artificial_sensor import Artificial_Sensor

def check_name(d):	#Checks if the "name" key exists in a dictionary
    if "name" not in d or d.get("name") == None:
    	return False
    else:
    	return True

def check_sensors(d):	#Checks if the sensors are written correctly in the config file
	if "sensors" in d:
		for sensor in d.get("sensors"):
			if "type" not in sensor or sensor.get("type") == None:
				return False
			else:
				return True
	else:
		return True

def check_config(dictionary):	#Scans the config file for errors or missing fields
    for key, value in dictionary.items():
        print (key + " : " + str(value))

    error_loc = "farm"	#error_loc variable helps user identify where error in config is occuring

    if not check_name(dictionary):	#Checks for "name" of farm
    	return 1, error_level

    error_loc = dictionary.get("name")

    if "environments" not in dictionary:	#Checks that environments field is present
    	return 2, error_loc

    if len(dictionary.get("environments")) == 0:	#Checks that an environment exists
    	return 3, error_loc

    for environment in dictionary.get("environments"):
    	error_loc = "environment"

    	if not check_name(environment):	#Checks environments have names
    		return 4, error_loc

    	error_loc = environment.get("name")

    	if "beds" not in environment:	#Checks that a bed field in each environment
    		return 5, error_loc

    	if len(environment.get("beds")) == 0:	#Checks that a bed exists
    		return 6, error_loc

    	if not check_sensors(environment):	#Checks environment-wide sensors
    		return 10, error_loc

    	for bed in environment.get("beds"):
    		error_loc = "bed"

    		if not check_name(bed):	#Checks beds have names
    			return 7, error_loc

    		error_loc = bed.get("name")

    		if "plants" not in bed:	#Checks that "plants" field exists in each bed
    			return 8, error_loc

    		if len(bed.get("plants")) == 0:	#Checks that a plant exists
    			return 9, error_loc

    		if not check_sensors(bed):	#Checks individual bed sensors
    			return 10, error_loc

    		for plant in bed.get("plants"):

    			error_loc = "plant"

    			if not check_name(plant):
    				return 11, error_loc
    return 0, None

def error_handle(error_message, error_location):	#Handles error messages produced by check_config
	if error_message == 1:
		print("ERROR: No name specified for farm")
	
	elif error_message == 2:
		print("ERROR: Must have \"environments\" list in farm")

	elif error_message == 3:
		print("ERROR: Must specify at least 1 environments")

	elif error_message == 4:
		print("ERROR: Every environment must have a name")

	elif error_message == 5:
		print("ERROR: Must have \"beds\" list in every environment")

	elif error_message == 6:
		print("ERROR: Must have at least 1 bed for each environment")

	elif error_message == 7:
		print("ERROR: Every bed must have a name")

	elif error_message == 8:
		print("ERROR: Must have \"plants\" list in every bed")

	elif error_message == 9:
		print("ERROR: Must have at least 1 plant for every bed")

	elif error_message == 10:
		print("ERROR: Sensor type not specified")

	elif error_message == 11:
		print("ERROR: Every plant must have a name")

	else:
		print("Loading in config file...")

	if error_message != 0:
		print("(%s)" % error_location)
		quit()

def add_sensors(farm_object, dictionary, sensors_list):
	if "sensors" in dictionary:	#Creates and associates environment-wide sensors
		for sensor in dictionary.get("sensors"):
			s = Artificial_Sensor(value = sensor.get("value"), noise = 0)
			s.set_datatype(sensor.get("type"))	#Sets type of data sensor is collecting
			s.set_location(str(dictionary.get("name"))) #sets location to the name of the environment
			if "refresh" in sensor:
				s.set_refresh(sensor.get("refresh"))

			s.set_noise(2) ###Set Noise (NOTE: Delete later, only for artificial sensor)


			farm_object.add_sensor(sensor.get("type"), s)
			sensors_list.append(s)

def load_config(config_file):
	stream = open(config_file, 'r')
	try:
		dictionary = yaml.safe_load(stream)
	except yaml.YAMLError as e:
		print(e)
		quit()

	error_handle(*check_config(dictionary))	#Reads in config.yaml file and checks for errors

	sensors = []
	farm_object = Farm(dictionary.get("name"))	#Sets name of farm

	for environment in dictionary.get("environments"):	#Sets up each individual environment
		env_object = Environment(str(environment.get("name")))	#Creates an environment with set name
		add_sensors(env_object, environment, sensors)

		for bed in environment.get("beds"):	#Creates and associates beds with environments
			bed_object = Bed(str(bed.get("name")))
			add_sensors(bed_object, bed, sensors)

			for plant in bed.get("plants"):	#Creates and associates plants with beds
				plant_object = Plant(str(plant.get("name")))
				bed_object.add_plant(plant_object)

			env_object.add_bed(bed_object)	#Adds beds to environments

		farm_object.add_environment(env_object)	#Adds environments to the farm

	print("FARM SETUP COMPLETE")

	'''
	for env_name, env in farm_object.get_envs().items():
		for bed_name, bed in env.get_beds().items():
			print("%s: %s" % (env_name, bed_name))
			for plant_name, plant in bed.get_plants().items():
				print("%s: %s" % (bed_name, plant_name))
	'''

	return farm_object, sensors

if __name__ == "__main__":
	load_config("config.yaml")



