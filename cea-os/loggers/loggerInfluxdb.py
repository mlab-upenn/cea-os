from influxdb_client import InfluxDBClient
from ..sensors.sensor_definition import Sensor

class LoggerInfluxDB():
  def __init__(self) -> None:
    self.client = None
    self.write_api = None
    self.sensor = None
    self.pollrate = 10  #seconds between data logs
    self.measurements = 0
    
  def configure(self, host, port, dbname):
    self.client = InfluxDBClient(host = host, port = port, dbname = dbname)
    self.write_api = self.client.write_api()
    
  def send_logs(self):
    write_api.write("M{measurement},Value=self.sensor.read_value()".format(measurement = self.measurements), protocol = "line")
    self.measurements += 1
  
  def set_sensor(self, Sensor):
    self.sensor = Sensor
    
  def set_pollrate(self, pollrate):
    self.pollrate = pollrate
    
    
