from .sensor_definition import Sensor
from ..loggers.InfluxDB import InfluxDBLogger


class NetworkSensor(Sensor):
    def __init__(self, logger, datatype=None, location=None):
        self.curr_value = None
        self.logger = logger
        self.datatype = datatype
        self.location = location
        self.calibrate = None

    def read_value(self):
        return self.curr_value

    def calibrate(self):
        return self.calibrate

    def recv_value(self, value, influxconnection):
        try:
            self.curr_value = value
            self.logger.send_logs(self.curr_value, self.datatype,
                                  self.location, influxconnection)
            return "successfully logged and updated"
        except:
            return "An error occurred with Network Sensor"
