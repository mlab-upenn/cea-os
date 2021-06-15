"""
This file contains the basic interface for sensors in this code base.
"""


class Actuator:
    def __init__(self) -> None:
        raise NotImplementedError

    def initialize(self):
        #This initializes everything required for actuator to be functional
        raise NotImplementedError

    def run(self):
        #This must be implemented in inheriting classes
        raise NotImplementedError

    def stop(self):
        #This must be implemented in inheriting classes
        raise NotImplementedError

    def is_running(self):
        return self.running

    def calibrate(self):
        """
        This method is used to calibrate the actuator. Need not be implemented for actuators that don't require calibration
        """
        pass