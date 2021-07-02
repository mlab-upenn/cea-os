"""
This file contains the basic interface for sensors in this code base.
"""


class Sensor:
    def __init__(self) -> None:
        raise NotImplementedError

    def read_value(self):
        """
        This method returns the value of the sensor
        """
        raise NotImplementedError
