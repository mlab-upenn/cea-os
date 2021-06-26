"""
This file contains a class for a camera sensor that encodes image data
"""
import base64
# from sensor_definition import Sensor
from ceaos.sensors.sensor_definition import Sensor


class ArtificialCamera(Sensor):

    datatype = "Image"  # static variable for Camera class

    def __init__(self, image_filepath="") -> None:
        self.set_image(image_filepath)

    def set_image(self, image_filepath: str):
        """
        This method sets the filepath where the camera image is stored
        """
        try:
            self.image_filepath = str(image_filepath)
            if self.image_filepath != "":
                self.set_value()  # encodes image to base64
            else:
                self.value = ""
        except ValueError:
            self.image_filepath = None
            raise ValueError("INVALID VALUE")

    def set_value(self):
        """
        This method sets the camera value by encoding
        the image stored at image_filepath
        """
        try:
            with open(self.image_filepath, "rb") as imagefile:
                byteform = base64.b64encode(imagefile.read())
            self.value = byteform
            # value is the bytes literal of encoded image
        except FileNotFoundError:
            """
            Setting to empty string instead of None since InfluxDB has
            issues with NaN (which might also apply to None)
            """
            self.value = ""
            raise FileNotFoundError("INVALID FILEPATH")
        except OSError:
            self.value = ""
            raise OSError("ERROR OPENING IMAGE")

    def get_filepath(self):
        return self.image_filepath

    def read_value(self):
        """
        This method returns the base64 encoded value of the camera image
        """
        return self.value

    def get_datatype(self):
        """
        This method returns the measurement
        the sensor is recording (i.e. temperature, pH)
        """
        return self.datatype

    def decode_value(self):  # not sure if we need this
        """
        This method decodes the base64 encoded image
        and returns the decoded string
        """
        return base64.b64decode(self.value)
