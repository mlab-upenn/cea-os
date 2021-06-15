from .actuator_definition import Actuator
import time

class Artificial_Actuator(Actuator):
    def __init__(self):
    	self.running = None
    	self.start_time = None
    	self.stop_time = None
    	self.id = None
        self.datatype = None

    def initialize(self):
        """
        This method returns the value of the sensor
        """
        

    def run(self, value: float):
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError("INVALID VALUE")

    def stop(self, noise: float):
        try:
            self.noise = abs(float(noise))
        except ValueError:
            raise ValueError("INVALID VALUE")

    def is_running(self):
    	pass

    def calibrate(self, calib_val):
        """
        This method is used to calibrate the sensor.
        """
        val = self.read_value()
        self.calib = calib_val - val
        print("Calibration value: {0}/nSensor value: {1}".format(
            calib_val, val))
        pass

    # returns the measurement the actuator is actuating (i.e. temperature, pH)
    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype
