"""
This file contains an plant model
"""


class Plant:
    def __init__(self, name):
        # general properties dictionary
        self.name = name
        self.properties = dict()

    def set_name(self, name):
        self.name = name

    def add_property(self, key, value):
        self.properties[key] = value

    def delete_property(self, key):
        del self.properties[key]
