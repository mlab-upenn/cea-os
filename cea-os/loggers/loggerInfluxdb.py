from influxdb_client import InfluxDBClient
from ..sensors import sensors

class LoggerInfluxDB():
  def __init__(self) -> None:
    self.client = None
    self.write_api = None
    self.sensor = None
    self.pollrate = 10  #seconds between data logs
    
  def configure(self, url, token, org):
    self.client = InfluxDBClient(url = url, token = token, org = org)
    self.write_api = self.client.write_api()
    
  def send_logs(self):
    pass
  
  def set_sensor(self, Sensor):
    self.sensor = Sensor
    
  def set_pollrate(self, pollrate):
    self.pollrate = pollrate
    
    
