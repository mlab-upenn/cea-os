from .actuator_definition import Actuator
from ..sensors.sensor_definition import Sensor
import time

"""
kind of hard to set up a fake actuator since there is no values to be read,
however, an example would be a motor, so in the initialize method we would set up stuff like pwm and
the time we want the actuator running for. This is probably dependedent on a sensor, for example say we wanted to 
set up some kind of pump to pump nutrients into the solution, this would happen on either a timer or a sensor.
"""
class Artificial_Actuator(Actuator):
    def __init__(self):
    	self.running = None
    	self.start_time = None
    	self.stop_time = None
    	self.id = None
        self.datatype = None
        self.curr_state = None

    def initialize(self):
    	#initialize things like pwm here
    	pass    

    def set_point(self, sensor):
        while sensor.read_value() > 20:
        	#actuate
        	print("actuating")
        self.stop()
        return self.curr_state

    def stop(self, noise: float):
        self.running = False
        #stop the necessary things

    def is_running(self):
    	return self.running

    def calibrate(self, calib_val):
        pass

    # returns the measurement the actuator is actuating (i.e. temperature, pH)
    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype
