class Logger():
  def __init__(self) -> None:
      raise NotImplementedError
      
  def configure(self):
      raise NotImplementedError
      
  def send_logs(self):
      raise NotImplementedError
      
  def add_sensor(self, Sensor, poll_rate):
      raise NotImplementedError
      
  def change_pollrate(self, Sensor):
      pass
    
