"""
This file contains an bed model
"""


class Bed:
    def __init__(self, name="bed0"):
        self.plants = dict()  # keeps track of plants in bed (name is key)
        self.sensors = dict()  # Sensors will be associated with beds
        self.actuators = dict()
        self.properties = dict()
        self.name = name

    def add_plant(self, plant):
        self.plants[plant.name] = plant

    def delete_plant(self, plant):
        # Once you delete plant, maybe add its
        # info somewhere for storage purposes?
        del self.plants[plant.name]

    def add_sensor(self, name, new_sensor):
        self.sensors[name] = new_sensor

    def delete_sensor(self, name):
        del self.sensors[name]

    def add_actuators(self, name, new_actuator):
        self.actuators[name] = new_actuator

    def delete_actuators(self, name):
        del self.actuators[name]

    def add_property(self, key, value):
        self.properties[key] = value

    def delete_property(self, key):
        del self.properties[key]

    def set_name(self, name):
        self.name = str(name)
