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
        self.noise = None

    def set_point(self, sensor):
        self.running = True
        while sensor.read_value() > 20:
            # actuate
            print("actuating")
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
