from connection_interface import DBConnection
from influxdb import InfluxDBClient


class InfluxDBConnection(DBConnection):
	def __init__(self) -> None:
		self.client = None

	def configure(self, host = 'localhost', port = 8086, username = 'grafana', password = 'password', database = 'grafana'):
		if database != 'grafana':	#creates new database if default grafana db is not being used
			self.client = InfluxDBClient(host = host, port = port, username = username, password = password)
			if database not in self.client.get_list_database().values():
				client.create_database(database)
		else:	#defaults to connecting to the local InfluxDB database set up in docker file, "grafana"
			self.client = InfluxDBClient(host = host, port = port, username = username, password = password, database = database)

		self.client.switch_database(database)

	def get_connection(self):	#returns database connection
		return self.client	
