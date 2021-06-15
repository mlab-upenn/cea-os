import base64

filename = "Dropbox\IoT4Ag\Code_Scrap\\a_plant.jpg" # update filepath to reflect local storage

with open(filename, 'rb') as imagefile:
    byteform = base64.b64encode(imagefile.read()) # convert whole image into byte form, a byte literal (not string)

f = open('Dropbox\IoT4Ag\Code_Scrap\encoded_image.bin', 'wb') #binary file, only holds bytes
f.write(byteform)
f.close()

