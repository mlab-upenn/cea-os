"""
This file contains an bed model
"""
 
from plants import Plant
from ..sensors.sensor_definition import Sensor

class Bed:
	def __init__(self):
		self.plants = dict() #keeps track of plants in bed (name is key)
		self.num_plants = 0
		self.num_sensors = 0
		self.sensors = list() #Sensors will be associated with beds
		self.actuators = list()
		self.num_actuators = list()
		self.properties = dict()

	def add_plant(self, plant):
		self.plants[plant.name] = plant
		self.num_plants += 1

	def delete_plant(self, plant):
		# Once you delete plant, maybe add its info somewhere for storage purposes?
		del self.plants[plant.name]

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