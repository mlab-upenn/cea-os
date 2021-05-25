"""
This file contains the basic interface for sensors in this code base.
"""
import random

class Sensor:
    def __init__(self, value = 0, noise = 0) -> None:
        self.value = value  #sets initial value for sensor data
        self.noise = noise  #sets level of noise (noise = 0 gives constant value)
    
    def read_value(self):
        """
        This method returns the value of the sensor
        """
        self.value += random.gauss(0, noise)    #adds/subtracts random val from gauss. dist.
        return self.value
    
    def set_value(self, value):
        try:
            self.value = (float) value
        except ValueError:
            print("INVALID VALUE")
    
    def set_noise(self, noise):
        try:
            self.noise = (float) abs(noise)
        except ValueError:
            print("INVALID VALUE")
            
    def calibrate(self):
        """
        This method is used to calibrate the sensor. Need not be implemented for sensors that don't require calibration
        """
        pass
