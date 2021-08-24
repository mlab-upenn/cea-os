

from os import name


class WemoActuator:
    def __init__(self):
        self.name = None
        self.refresh_rate = None

    def setpoint(self, arg):
        # This must be implemented in inheriting classes
        raise NotImplementedError

    def do(self, arg):
        # This must be implemented in inheriting classes
        raise NotImplementedError

    def calibrate(self):
        """
        This method is used to calibrate the actuator.
        Need not be implemented for actuators that don't require calibration
        """
        pass