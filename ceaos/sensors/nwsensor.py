from .sensor_definition import Sensor
from ..loggers.InfluxDB import InfluxDBLogger


class NetworkSensor(Sensor):
    def __init__(self,
                 logger=None,
                 datatype=None,
                 location=None,
                 influxconnection=None):
        self.curr_value = None
        self.logger = logger
        self.datatype = datatype
        self.location = location
        self.refresh = None
        self.influxconnection = influxconnection
        self.name = None

    def read_value(self):
        return self.curr_value

    def calibrate(self):
        print("Calibration must be done by the user on the sensor side.")

    def recv_value(self, value=None, **kwargs):
        try:
            if kwargs:
                for val in kwargs:
                    self.datatype = val
                    self.curr_value = kwargs[val]
                    self.logger.send_logs("sensor_data", self.datatype,
                                          self.location, self.influxconnection)
                self.curr_value = kwargs

            # Don't send stuff as single value, preferable a key word arg.
            if value:
                self.curr_value = value
                self.logger.send_logs("sensor_data", self.datatype,
                                      self.location, self.influxconnection)

            return "Successful Connection to Network Sensor"
        except:
            return "An error occurred with Network Sensor"

    def set_datatype(self, datatype):
        self.datatype = datatype

    def set_name(self, name):
        try:
            self.name = str(name)
        except ValueError:
            print("Invalid sensor name")

    def set_logger(self, logger):
        self.logger = logger

    def set_influxconnection(self, influxconnection):
        self.influxconnection = influxconnection

    def get_datatype(self):
        return self.datatype

    def get_refresh(self):
        return self.refresh
