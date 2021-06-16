from .sensor_definition import Sensor
from time import sleep
from datetime import datetime

class PiCam(Sensor):

	def __init__(self) -> None:
		self.camera = PiCamera()
		self.camera.rotation = 180

	def read_value(self):
		now = datetime.now()
		date_str = now.strftime("%m_%d_%Y__%H:%M")
		self.camera.start_preview()
		self.camera.annotate_text = date_str
		sleep(3)
		camera.capture('/home/pi/Documents/Plant_Photos/%s.jpg' % date_str)
		self.camera.stop_preview()

	def calibrate(self, rotation):
		#rotate camera with this
		self.camera.rotation = rotation