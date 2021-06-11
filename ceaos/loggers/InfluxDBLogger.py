from logger_interface import Logger
from InfluxDBConnection import InfluxDBConnection
from datetime import datetime
from datetime import timedelta
from ..sensors.sensor_definition import Sensor


class InfluxDBLogger(Logger):

	def __init__(self, sensor = None) -> None:
		self.refresh_rate = 10
		self.sensor = sensor
		self.bed = None

	def set_refresh_rate(self, rate: float): #sets refresh_rate of logger
		try:
			self.refresh_rate = float(rate)
		except ValueError:
			print("Error: Invalid refresh rate")

	def send_logs(self, measurement: str, plant: str, data_type: str, influxConnection: InfluxDBConnection): #sends data from sensor to database
		if self.sensor == None:
			print("Error: No sensor linked to logger")
		else:
			json_data = []
			data = {
				"measurement": measurement,
				"tags": {
					"plant": plant
				},
				"time": datetime.now() + timedelta(hours = 4),
				"fields": {
					data_type: self.sensor.read_value()
				}
			}
			json_data.append(data)
			write_success = influxConnection.get_connection().write_points(json_data)
			if not write_success:	#throws error if unable to write to database
				print("Error: Write to database failed")
	
	def set_sensor(self, sensor: Sensor):	#sets the sensor being logged
		#if type(sensor) is Sensor:
		self.sensor = sensor
		#else:
			#print("Error: Invalid sensor")

	def get_sensor(self):	#returns the sensor being logged
		return self.sensor

	def get_refresh_rate(self):	#returns the refresh_rate of the logger
		return self.refresh_rate
	
	def set_bed(self, bed):	#sets the bed associated with logger
		self.bed = bed

	def get_bed(self):	#returns the bed associated with logger
		return self.bed
