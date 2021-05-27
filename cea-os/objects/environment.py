"""
This file contains an environment model
"""

from beds import Bed
from ..sensors.sensor_definition import Sensor

class Environment:
	#temperature, nutrients, water, lighting, light intensity will be added later
	def __init__(self, name, farm):
		#self.temperature = temperature
		#self.water = water
		#self.nutrients = nutrients
		self.name = name
		# I use a dictionary because we do not want duplicates names
		self.beds = dict() #keeps track of beds (name is key)
		self.num_beds = 0
		self.farm = farm #farm name environment is associated with
		#self.lighting = lighting
		self.sensors = list() # Some sensors will be on an environment level
		self.num_sensors = 0
		self.actuators = list()
		self.num_actuators = list()
		#self.light_intensity = light_intensity #measured in lumens per square meter?

	def add_bed(self, bed):
		self.beds[bed.name] = bed
		self.num_beds += 1

	def delete_bed(self, bed):
		del self.beds[bed.name]

	def set_temperature(self, temperature):
		self.temperature = temperature

	def set_water(self, water):
		self.water = water

	def set_nutrients(self, nutrients):
		self.nutrients = nutrients

	def set_name(self, name):
		self.name = name

	def set_lighting(self, lighting):
		self.lighting = lighting

	def add_sensor(self, name, new_sensor):
		toadd = (name, new_sensor)
		self.sensors.append(toadd)
		self.num_sensors += 1 

	def add_actuators(self, name, actuator):
		toadd = (name, actuator)
		self.actuators.append(toadd)
		self.num_actuators += 1

	def current_temperature(self, sensor):
		#poll environment level sensor to see if it is within accetable range
		#have some kind of logic that will actuate the system or raise an alarm if not within range
		raise NotImplementedError

	def current_water(self, sensor):
		#poll environment level sensor to see if it is within accetable range
		#have some kind of logic that will actuate the system or raise an alarm if not within range
		raise NotImplementedError

	def current_nutrient(self, sensor):
		#poll environment level sensor to see if it is within accetable range
		#have some kind of logic that will actuate the system or raise an alarm if not within range
		raise NotImplementedError

	def current_light_intensity(self, sensor):
		#poll environment level sensor to see if it is within accetable range
		#have some kind of logic that will actuate the system or raise an alarm if not within range
		raise NotImplementedError






