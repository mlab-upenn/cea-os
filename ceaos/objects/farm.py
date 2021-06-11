"""
This file contains a farm model
"""


class Farm:
    def __init__(self, name):
        self.name = name
        self.environments = dict()  #keeps track of environments (name is key)
        self.num_environments = 0

    # allows you to add environments
    def add_environment(self, environment):
        self.environments[environment.name] = environment
        self.num_environments += 1

    # allows you to delete environments
    def delete_environment(self, environment):
        del self.environments[environment.name]

    # if you want to change the farm name
    def set_name(self, name):
        self.name = name

    #return dictionary of environments
    def get_envs(self):
        return self.environments

    #return name of farm
    def get_name(self):
        return self.name
