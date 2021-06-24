import base64

# update filepath to reflect local storage:
filename = 'Dropbox\IoT4Ag\Code_Scrap\encoded_image.bin'
file = open(filename, 'rb')  # read binary mode
byte = file.read()  # returns all data in byte form
file.close()

# name of new image, write binary mode:
f = open('Dropbox\IoT4Ag\Code_Scrap\\decoded_image.jpg', 'wb')
f.write(base64.b64decode(byte))
f.close()
