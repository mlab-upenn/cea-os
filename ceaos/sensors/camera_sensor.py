"""
This file contains a class for a camera sensor that encodes image data
"""
import base64
from sensor_definition import Sensor # the original ".sensor_definition" threw me an error, but removing the "." solved it


class Camera(Sensor):

    datatype = "Image"  # static variable for Camera class

    def __init__(self, image_filepath="") -> None:
        self.set_filepath(image_filepath)
        if self.image_filepath != "":
            self.set_value(self.image_filepath)  # encodes image to base64
        else:
            self.value = ""

    def set_filepath(self, image_filepath: str):
        """
        This method sets the filepath where the camera image is stored
        """
        try:
            self.image_filepath = str(image_filepath)
        except ValueError:
            raise ValueError("INVALID VALUE")

    def set_value(self, image_filepath: str):
        """
        This method sets the camera value by encoding the image stored at image_filepath
        """
        try:
            with open(self.image_filepath, "rb") as imagefile:
                byteform = base64.b64encode(imagefile.read())
            self.value = byteform  # value is the bytes literal of encoded image
        except FileNotFoundError:
            self.value = ""
            raise FileNotFoundError("INVALID FILEPATH")
        except OSError:
            self.value = ""
            raise OSError("ERROR OPENING IMAGE")
        except ValueError:
            self.value = ""
            raise ValueError("INVALID VALUE")

    def get_filepath(self):
        return self.image_filepath

    def read_value(self):
        """
        This method returns the base64 encoded value of the camera image
        """
        return self.value

    def get_datatype(self): # returns the measurement the sensor is recording (i.e. temperature, pH)
        return self.datatype

    def decode_value(self): # not sure if we need this
        """
        This method decodes the base64 encoded image and returns the decoded string
        """
        return base64.b64decode(self.value)

