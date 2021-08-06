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

    def set_point(self, min=None, max=None):
        raise NotImplementedError

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
