"""
This file contains a class for a temperature sensor
"""
from .sensor_definition import Sensor  
from ceaos.loggers.InfluxDB import InfluxDBConnection, InfluxDBLogger


class Temperature(Sensor):

    datatype = "General_Temp"  # static variable for Temperature class

    def __init__(self, temp_value=None, datatype=datatype) -> None:
        self.set_value(temp_value)
        self.set_datatype(datatype) # defaults to "General_Temp" (i.e. instead of Air_Temp)

    def set_value(self, temp_value: float):
        """
        This method sets the sensor value (i.e. the air temperature)
        """
        if temp_value != None:
            try:
                self.value = float(temp_value)
            except ValueError:
                self.value = None
                raise ValueError("INVALID VALUE")
        else:
            self.value = None
   
    def set_datatype(self, datatype: str):
        self.datatype = datatype

    def read_value(self):
        """
        This method returns the sensor value (i.e. the air temperature)
        """
        return self.value

    def get_datatype(self):  # returns the measurement the sensor is recording (i.e. temperature, pH)
        return self.datatype