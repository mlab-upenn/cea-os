import base64

filename = 'Dropbox\IoT4Ag\Code_Scrap\encoded_image.bin'

file = open(filename, 'rb') #read binary mode
byte = file.read() #returns all data in byte form
file.close()

f = open('Dropbox\IoT4Ag\Code_Scrap\\decoded_image.jpg', 'wb') #name of new image, write binary mode
f.write(base64.b64decode(byte))
f.close()


