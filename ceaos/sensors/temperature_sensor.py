"""
This file contains a class for a temperature sensor
"""
import os
import sys
os.chdir("pigpio_dht22")
sys.path.append("/home/pi/pigpio_dht22")
import pigpio # module only found on Pi
import DHT22 # module only found on Pi
from sensor_definition import Sensor


class Temperature(Sensor):
    def __init__(self,
                 gpio=4,
                 temp_value=None,
                 datatype="General_Temp") -> None:
        self.set_datatype(datatype)
        self.pi = pigpio.pi()
        self.set_gpio(gpio)
        self.sensor = DHT22.sensor(self.pi, self.gpio)
        self.set_value(temp_value)

    def set_gpio(self, gpio: int):
        try:
            self.gpio = int(gpio)
        except ValueError:
            self.gpio = None
            raise ValueError("INVALID VALUE")

    def set_value(self, temp_value: float):
        """
        This method sets the sensor value (i.e. the air temperature)
        """
        if temp_value is not None:
            try:
                self.value = float(temp_value)
            except ValueError:
                self.value = None
                raise ValueError("INVALID VALUE")
        else:
            self.sensor.trigger()
            self.value = self.get_temp(self.sensor)
            # ISSUE: gets caught in an infinite loop
            while (self.value == -999.0):
                self.sensor.trigger()
                self.value = self.get_temp(self.sensor)

    def set_datatype(self, datatype: str):
        self.datatype = datatype

    def get_temp(
        self, phys_sensor: DHT22
    ):  # what datatype is phys_sensor? what does DHT22.sensor() return?
        if phys_sensor.temperature() is not None:
            newTemp = phys_sensor.temperature()
        else:
            newTemp = None
            print("Error: sensor read failed")
        return newTemp

    def read_value(self):
        """
        This method returns the sensor value (i.e. the air temperature)
        """
        return self.value

    def get_datatype(self):
        """
        This method returns the measurement the sensor
        is recording (i.e. temperature, pH)
        """
        return self.datatype
