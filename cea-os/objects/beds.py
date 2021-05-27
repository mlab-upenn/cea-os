"""
This file contains an bed model
"""

from ..sensors import sensor_definition 
from plants import Plant

class Bed:
	def __init__(self, name, environment, area = 0, system = 'NFT'):
		self.area = area
		self.system = system
		self.name = name
		self.plants = dict() #keeps track of plants in bed (name is key)
		self.num_plants = 0
		self.num_sensors = 0
		self.sensors = list() #Sensors will be associated with beds
		self.environment = environment

	def add_plant(self, plant):
		self.plants[plant.name] = plant
		self.num_plants += 1

	def delete_plant(self, plant):
		del self.plants[plant.name]

	def add_sensor(self, name, new_sensor):
		self.sensors.append(name, new_sensor)
		self.num_sensors += 1

	def set_system(self, system):
		self.system = system

	def set_name(self, name):
		self.name = name#test