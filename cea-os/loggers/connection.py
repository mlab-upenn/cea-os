class DBConnection():
  def __init__(self) -> None:
    raise NotImplementedError
  
  def configure(self):  #establish connection to database
    raise NotImplementedError
    
  def return_connection(self):  #return the database client created by connection
    raise NotImplementedError
  
