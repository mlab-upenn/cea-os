from .sensor_definition import Sensor
from ..loggers.InfluxDB import InfluxDBLogger


class NetworkSensor(Sensor):
    def __init__(self, logger=None, datatype=None, location=None):
        self.curr_value = None
        self.logger = logger
        self.datatype = datatype
        self.location = location
        self.refresh = None

    def read_value(self):
        return self.curr_value

    def calibrate(self):
        print("Calibration must be done by the user on the sensor side.")

    def recv_value(self, value, influxconnection):
        try:
            self.curr_value = value
            self.logger.send_logs("sensor_data", self.datatype, self.location,
                                  influxconnection)
            return "successfully logged and updated"
        except:
            return "An error occurred with Network Sensor"

    def set_datatype(self, datatype):
        self.datatype = datatype

    def set_location(self, location):
        self.location = location

    def set_logger(self, logger):
        self.logger = logger

    def get_location(self):
        return self.location

    def get_datatype(self):
        return self.datatype

    def get_refresh(self):
        return self.refresh
