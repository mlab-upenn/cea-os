from camera_sensor import Camera
from temp_sensor import Temperature

### Tests ###
#a_camera = Camera()
# a_camera = Camera("Dropbox\IoT4Ag\Code_Scrap\\a_plant.jpg")
# print(a_camera.read_value())
# print(a_camera.get_filepath())
# print(a_camera.get_datatype())
#print(Camera.datatype)
#print(a_camera.decode_value()) # this does weird things. just wanted to see what happens 

# encoded = "YmFzZTY0IGVuY29kZWQgc3RyaW5n"
# decoded = base64.b64decode(encoded)
# print(decoded)

airTemp = Temperature(15, "Air_Temp")
print(airTemp.read_value())
print(airTemp.get_datatype())
