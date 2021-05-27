"""
This file contains an environment model
"""

from beds import Bed
#from ..sensor_definition import Sensor

class Environment:
	def __init__(self, name, farm, temperature = 0, water = 0, nutrients = 0, lighting = 'LED'):
		self.temperature = temperature
		self.water = water
		self.nutrients = nutrients
		self.name = name
		self.beds = dict() #keeps track of beds (name is key)
		self.num_beds = 0
		self.farm = farm #farm name environment is associated with
		self.lighting = lighting

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