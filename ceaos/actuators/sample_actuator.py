from .actuator_definition import Actuator
from ..sensors.sensor_definition import Sensor


class Artificial_Actuator(Actuator):
    def __init__(self):
        self.id = None
        self.stop_time = None
        self.start_time = None
        self.running = None
        self.curr_state = None
        self.datatype = None
        self.location = None
        self.ip = None
        self.sensor = None

    def set_point(self, min, max):
        self.running = True
        print(max)
        print(min)
        self.stop()
        return self.running

    def stop(self):
        self.running = False
        # stop the necessary things

    def set_noise(self, noise: float):
        try:
            self.noise = abs(float(noise))
        except ValueError:
            raise ValueError("INVALID VALUE")

    def is_running(self):
        return self.running

    def calibrate(self, calib_val):
        pass

    # returns the measurement the actuator is actuating (i.e. temperature, pH)
    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self, ip):
        return self.ip

    def set_sensor(self, sensor):
        self.sensor = sensor

    def get_sensor(self, sensor):
        return self.sensor
