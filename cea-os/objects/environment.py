"""
This file contains an environment model
"""

from beds import Bed
from ..sensors.sensor_definition import Sensor

class Environment:
	#temperature, nutrients, water, lighting, light intensity will be added later
	def __init__(self):
		# I use a dictionary because we do not want duplicates names
		self.beds = dict() #keeps track of beds (name is key)
		self.num_beds = 0
		self.sensors = list() # Some sensors will be on an environment level
		self.num_sensors = 0
		self.actuators = list()
		self.num_actuators = list()
		self.properties = dict()
		self.name = "env0"

	def add_bed(self, bed):
		self.beds[bed.name] = bed
		self.num_beds += 1

	def delete_bed(self, bed):
		del self.beds[bed.name]

	def add_sensor(self, name, new_sensor):
		toadd = (name, new_sensor)
		self.sensors.append(toadd)
		self.num_sensors += 1 

	def add_actuators(self, name, actuator):
		toadd = (name, actuator)
		self.actuators.append(toadd)
		self.num_actuators += 1

	def add_property(self, key, value):
		self.properties[key] = value

	def delete_property(self, key):
		del self.properties[key]
	
	def set_name(name):
		self.name = name	





