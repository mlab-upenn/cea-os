class Logger():
  def __init__(self) -> None:
      raise NotImplementedError
      
  def connect(self):  #establish connection to db
      raise NotImplementedError
      
  def create_table(self): #create db table
      raise NotImplementedError
      
  def set_refresh_rate(self): #set refresh rate of data logging
      raise NotImplementedError
      
  def send_logs(self):  #send logs to database
      raise NotImplementedError
      
  def add_sensor(self, Sensor): #add a sensor that is being logged
      raise NotImplementedError
    
