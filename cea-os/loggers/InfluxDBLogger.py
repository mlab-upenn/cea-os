from logger_interface import Logger
from InfluxDBConnection import InfluxDBConnection
from datetime import datetime
from datetime import timedelta
from ..sensors.sensor_definition import Sensor


class InfluxDBLogger(Logger):

	def __init__(self) -> None:
		self.refresh_rate = 10 #units: min
		self.sensor = None

	def set_refresh_rate(self, rate: float): #sets refresh_rate of logger
		self.refresh_rate = rate

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
				"time": datetime.now(),
				"fields": {
					data_type: self.sensor.read_value()
				}
			}
			json_data.append(data)
			write_success = influxConnection.get_connection.write_points(json_data)
			if not write_success: #throws error if unable to write to database
				print("Error: Write to database failed")
	
	def set_sensor(self, sensor: Sensor): #sets the sensor being logged
		self.sensor = sensor

	def get_sensor(self): #returns the sensor being logged
		return self.sensor

	def get_refresh_rate(self): #returns the refresh_rate of the logger
		return self.refresh_rate
