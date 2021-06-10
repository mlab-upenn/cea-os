"""
This file contains a class for an artificial sensor
"""
import random
from .sensor_definition import Sensor

class Artificial_Sensor(Sensor):
    def __init__(self, value = 20, noise = 0) -> None:
        try:
            self.value = float(value)   #sets initial value for sensor data
        except ValueError:
            self.value = 20
            print("INVALID VALUE")          
        try:
            self.noise = float(noise)   #sets level of noise (noise = 0 gives constant value)
        except ValueError:
            self.noise = 0
            print("INVALID NOISE")
        self.calib = 0  #sets calibration difference
    
    def read_value(self):
        """
        This method returns the value of the sensor
        """
        self.value += random.gauss(0, self.noise)    #adds/subtracts random val from gauss. dist.
        return self.value + self.calib
    
    def set_value(self, value: float):
        try:
            self.value = float(value)
        except ValueError:
            print("INVALID VALUE")
    
    def set_noise(self, noise: float):
        try:
            self.noise = abs(float(noise))
        except ValueError:
            print("INVALID VALUE")
            
    def calibrate(self, calib_val):
        """
        This method is used to calibrate the sensor.
        """
        val = self.read_value()
        self.calib = calib_val - val
        print("Calibration value: {0}/nSensor value: {1}".format(calib_val, val))
        pass
