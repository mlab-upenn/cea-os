import os
import pigpio
import DHT22
from .sensor_definition import Sensor
os.chdir("pigpio_dht22")  # so that new module is in the right path


class TempHumiditySensor(Sensor):
    def __init__(self, gpio=4):
        self.gpio = gpio
        self.pi = pigpio.pi()
        self.s = DHT22.sensor(self.pi, self.gpio)

    def read_value(self):
        self.s.trigger()
        if self.s.humidity() is not None and self.s.temperature() is not None:
            return ("{:3.2f}".format(self.s.humidity() / 1.0)), (
                "{:3.2f}".format(self.s.temperature() / 1.0)
            )
        else:
            return "error"

    def calibrate(self, calib_val_humidity, calib_val_temperature):
        humidity, temperature = self.read_value()
        self.calib_humidity = calib_val_humidity - humidity
        self.calib_temperature = calib_val_temperature - temperature
        pass
