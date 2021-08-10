"""
This file contains an environment model
"""


class Environment:
    def __init__(self, name="env0"):
        # I use a dictionary because we do not want duplicates names
        self.beds = dict()  # keeps track of beds (name is key)
        self.sensors = dict()  # Some sensors will be on an environment level
        self.actuators = dict()
        self.properties = dict()
        self.name = name

    def add_bed(self, bed):
        self.beds[bed.name] = bed

    def delete_bed(self, bed):
        del self.beds[bed.name]

    def add_sensor(self, name, new_sensor):
        self.sensors[name] = new_sensor

    def delete_sensor(self, name):
        del self.sensors[name]

    def add_actuators(self, name, actuator):
        self.actuators[name] = actuator

    def delete_actuators(self, name):
        del self.actuators[name]

    def add_property(self, key, value):
        self.properties[key] = value

    def delete_property(self, key):
        del self.properties[key]

    def set_name(self, name):
        self.name = str(name)
