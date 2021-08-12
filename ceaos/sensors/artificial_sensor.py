"""
This file contains a class for an artificial sensor
"""
import random
from .sensor_definition import Sensor


class ArtificialSensor(Sensor):
    def __init__(self, value=20, noise=0, refresh=10) -> None:
        try:
            self.value = float(value)  # sets initial value for sensor data
        except ValueError:
            self.value = 20
            raise ValueError("INVALID VALUE")
        try:
            self.noise = float(
                noise)  # sets level of noise (noise = 0 gives constant value)
        except ValueError:
            self.noise = 0
            raise ValueError("INVALID NOISE")
        self.calib = 0  # sets calibration difference
        self.datatype = None
        self.location = None
        self.refresh = refresh
        self.logger = None
        self.name = None

    def read_value(self):
        """
        This method returns the value of the sensor
        """
        self.value += random.gauss(
            0, self.noise)  # adds/subtracts random val from gauss. dist.
        return self.value + self.calib

    def set_value(self, value: float):
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError("INVALID VALUE")

    def set_noise(self, noise: float):
        try:
            self.noise = abs(float(noise))
        except ValueError:
            raise ValueError("INVALID VALUE")

    def calibrate(self, calib_val):
        """
        This method is used to calibrate the sensor.
        """
        val = self.read_value()
        self.calib = calib_val - val
        print("Calibration value: {0}/nSensor value: {1}".format(
            calib_val, val))
        pass

    # returns the measurement the sensor is recording (i.e. temperature, pH)
    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_refresh(self, refresh_rate):
        self.refresh = refresh_rate

    def get_refresh(self):
        return self.refresh

    def set_logger(self, logger):
        self.logger = logger

    def get_logger(self):
        return self.logger

    def set_name(self, name):
        self.name = name
