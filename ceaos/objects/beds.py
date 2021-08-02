"""
This file contains an bed model
"""


class Bed:
    def __init__(self, name="bed0"):
        self.plants = dict()  # keeps track of plants in bed (name is key)
        self.num_plants = 0
        self.num_sensors = 0
        self.sensors = dict()  # Sensors will be associated with beds
        self.actuators = dict()
        self.num_actuators = 0
        self.properties = dict()
        self.name = name

    def add_plant(self, plant):
        self.plants[plant.name] = plant
        self.num_plants += 1

    def delete_plant(self, plant):
        # Once you delete plant, maybe add its
        # info somewhere for storage purposes?
        del self.plants[plant.name]
        self.num_plants -= 1

    def recv_details(self, **kwargs):
        try:
            for val in kwargs:
                if val == "ip":
                    actuator_list = []
                    self.actuators[kwargs[val]] = actuator_list
                else:
                    self.actuators[kwargs["ip"]].append(kwargs[val])
            return "Succesfully recieved Microcontroller Data"
        except:
            return "An error occured receiving Microcontroller data"

    def add_sensor(self, name, new_sensor):
        self.sensors[name] = new_sensor
        self.num_sensors += 1

    def delete_sensor(self, name):
        del self.sensors[name]
        self.num_sensors -= 1

    def add_actuators(self, ip, actuator):
        if ip in self.actuators:
            self.actuators[ip].append(actuator)
        else:
            self.actuators[ip] = []
            self.actuators[ip].append(actuator)
        self.num_actuators += 1

    def add_property(self, key, value):
        self.properties[key] = value

    def delete_property(self, key):
        del self.properties[key]

    def set_name(self, name):
        self.name = str(name)

    def get_sensors(self):
        return self.sensors

    def get_actuators(self):
        return self.actuators

    def get_name(self):
        return self.name

    def get_plants(self):
        return self.plants
