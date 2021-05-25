"""
This file contains the basic interface for sensors in this code base.
"""
import random

class Sensor:
    def __init__(self, value = 0, constant = 1) -> None:
        self.value = value
        self.constant = constant
    
    def read_value(self):
        """
        This method returns the value of the sensor
        """
        if self.constant == 0:
            self.value += random.randint(-5,5)
        
        return self.value
    
    def calibrate(self):
        """
        This method is used to calibrate the sensor. Need not be implemented for sensors that don't require calibration
        """
        pass
