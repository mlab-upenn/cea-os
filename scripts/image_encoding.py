import base64

filename = "Dropbox\IoT4Ag\Code_Scrap\\a_plant.jpg"

with open(filename, 'rb') as imagefile:
    # convert whole image into byte form
    byteform = base64.b64encode(imagefile.read())

f = open('Dropbox\IoT4Ag\Code_Scrap\encoded_image.bin', 'wb')
f.write(byteform)  # binary file, only holds bytes
f.close()
