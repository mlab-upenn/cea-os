class Logger():
  def __init__(self) -> None:
      raise NotImplementedError
      
  def configure(self):  #configure connection to database and set up table for data
      raise NotImplementedError
      
  def send_logs(self):  #send logs to database
      raise NotImplementedError
      
  def set_sensor(self, Sensor): #set the sensor that is being logged
      raise NotImplementedError
      
  def set_pollrate(self): #set the pollrate for the sensors in the bed
      pass
    
