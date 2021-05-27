"""
This file contains an plant model
"""

class Plant:
	def __init__(self, name, bed, date_planted, plant_type = 'lettuce'):
		self.plant_type = plant_type
		self.name = name
		self.bed = bed
		self.date_planted = date_planted
		self.date_removed = "not known"

	def set_name(self, name):
		self.name = name

	def set_plant_type(self, plant_type):
		self.plant_type = plant_type

	def set_bed(self, bed):
		self.bed = bed

	def set_date_removed(self, date_removed):
		self.date_removed = date_removed