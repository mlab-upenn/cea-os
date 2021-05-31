class DBConnection():
  def __init__(self) -> None:
    raise NotImplementedError
  
  def configure(self):
    raise NotImplementedError
    
  def return_connection(self):
    raise NotImplementedError
  
