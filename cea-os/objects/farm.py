"""
This file contains a farm model
"""

from environment import Environment

class Farm:
	def __init__(self, name):
		self.name = name
		self.environments = dict() #keeps track of environments (name is key)
		self.num_environments = 0
		self.people = list()

	# allows you to add environments
	def add_environment(self, environment):
		self.environments[environment.name] = environment
		self.num_environments += 1

	# allows you to delete environments
	def delete_environment(self, environment):
		del self.environments[environment.name]

	def set_name(self, name):
		self.name = name

	def add_people(self, person):
		self.people.append(person)