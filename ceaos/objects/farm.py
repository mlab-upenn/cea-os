"""
This file contains a farm model
"""


class Farm:
    def __init__(self, name):
        self.name = name
        self.environments = dict()  # keeps track of environments (name is key)

    # allows you to add environments
    def add_environment(self, environment):
        self.environments[environment.name] = environment

    # allows you to delete environments
    def delete_environment(self, environment):
        del self.environments[environment.name]

    # if you want to change the farm name
    def set_name(self, name):
        self.name = str(name)
