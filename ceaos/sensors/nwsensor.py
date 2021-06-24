from .sensor_definition import Sensor
from ..loggers.InfluxDB import InfluxDBLogger


class Network_Sensor(Sensor):
    def __init__(self, sensor=None, ):
        self.curr_value = None
        self.logger = InfluxDBLogger()
        # I think each Network_Sensor is essentially
        # attached to an actual sensor
        self.sensor = sensor

    def read_value(self):
        return self.sensor.read_value()

    def calibrate(self):
        return self.sensor.calibrate()

    def recv_value(self, influxconnection):
        try:
            self.curr_value = self.read_value
            self.logger.send_logs(self.curr_value, self.sensor.datatype,
                                  self.sensor.location, influxconnection)
            return "successfully logged and updated"
        except:
            return "An error occurred with Network Sensor"
