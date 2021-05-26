"""
This file contains the basic interface for sensors in this code base.
"""
import random

class Sensor:
    def __init__(self, value, noise) -> None:
        raise NotImplementedError
    
    def read_value(self):
        """
        This method returns the value of the sensor
        """
        raise not ImplementedError
            
    def calibrate(self):
        """
        This method is used to calibrate the sensor. Need not be implemented for sensors that don't require calibration
        """
        pass
