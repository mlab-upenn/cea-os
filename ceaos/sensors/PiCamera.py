from .sensor_definition import Sensor
from time import sleep
from picamera import PiCamera
from datetime import datetime


class PiCam(Sensor):
    def __init__(
        self, sleep_val=3, file_path="/home/pi/Documents/Plant_Photos/"
    ) -> None:
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.sleep_val = sleep_val
        self.file_path = file_path

    def read_value(self):
        now = datetime.now()
        date_str = now.strftime("%m_%d_%Y__%H:%M")
        self.camera.start_preview()
        self.camera.annotate_text = date_str
        sleep(self.sleep_val)
        self.camera.capture(self.file_path + "%s.jpg" % date_str)
        self.camera.stop_preview()

    def calibrate(self, rotation):
        # rotate camera with this
        self.camera.rotation = rotation

    def set_sleep_val(self, sleep_val):
        self.sleep_val = sleep_val

    def set_file_path(self, file_path):
        self.file_path = file_path
