from influxdb import InfluxDBClient
from datetime import datetime, timedelta
import time
from pytz import timezone

from .interfaces import DBConnection, Logger
from ..sensors.sensor_definition import Sensor


class InfluxDBConnection(DBConnection):
    def __init__(self) -> None:
        self.client = None

    def configure(
        self,
        host="influxdb",
        port=8086,
        username="grafana",
        password="password",
        database="grafana",
    ):
        if (database != "grafana"
            ):  # creates new database if default grafana db is not being used
            self.client = InfluxDBClient(host=host,
                                         port=port,
                                         username=username,
                                         password=password)
            if database not in self.client.get_list_database().values():
                self.client.create_database(database)

        else:  # defaults to connecting to the local InfluxDB database set up in docker file, "grafana"
            self.client = InfluxDBClient(
                host=host,
                port=port,
                username=username,
                password=password,
                database=database,
            )

        self.client.switch_database(database)

    def get_connection(self):  # returns database connection
        return self.client


class InfluxDBLogger(Logger):
    def __init__(self, sensor=None) -> None:
        self.refresh_rate = None
        self.sensor = sensor
        self.location = None

    def set_refresh_rate(self, rate: float):  # sets refresh_rate of logger
        try:
            self.refresh_rate = float(rate)
        except ValueError:
            print("Error: Invalid refresh rate")

    def send_logs(
        self,
        data_collection_method: str,  # default recommended is "sensor_data"
        data_type: str,
        location: str,
        influxConnection: InfluxDBConnection,
    ):  # sends data from sensor to database
        if self.sensor is None:
            print("Error: No sensor linked to logger")
        else:
            json_data = []
            data = {
                "measurement": data_collection_method,
                "tags": {
                    "location": location
                },
                "time": datetime.now(),
                "fields": {
                    data_type: self.sensor.read_value()
                },
            }
            json_data.append(data)
            write_success = influxConnection.get_connection().write_points(
                json_data)
            if not write_success:  # throws error if unable to write to database
                print("Error: Write to database failed")

    def set_sensor(self, sensor: Sensor):  # sets the sensor being logged
        self.sensor = sensor

    def get_sensor(self):  # returns the sensor being logged
        return self.sensor

    def get_refresh_rate(self):  # returns the refresh_rate of the logger
        return self.refresh_rate

    def set_location(self,
                     location):  # sets the location associated with logger
        self.location = location

    def get_location(self):  # returns the bed associated with logger
        return self.location
