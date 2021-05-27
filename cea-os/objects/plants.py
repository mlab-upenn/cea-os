"""
This file contains an plant model
"""

class Plant:
	def __init__(self, name, bed, date_planted, plant_type = 'lettuce', weight = 0, health = 10):
		self.plant_type = plant_type
		self.name = name
		self.bed = bed
		self.date_planted = date_planted
		self.date_removed = "not known"
		self.weight = weight
		self.health = health  #Plant health on a scale of 1-10?

	def set_name(self, name):
		self.name = name

	def set_plant_type(self, plant_type):
		self.plant_type = plant_type

	def set_bed(self, bed):
		self.bed = bed

	def set_date_removed(self, date_removed):
		self.date_removed = date_removed

	def set_weight(self, weight):
		self.weight = weight

	def set_health(self, health):
		self.health = health