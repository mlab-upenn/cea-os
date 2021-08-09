# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
from .image_analysis_sensor import *

class Stitcher():
    def __init__(self):
        self.images = []
        self.stitched_img = None
        self.location = None
        self.output_dir = './images/stitched.png'
        self.analytics_sensor = None

    def set_location(self, location):
        self.location = location

    def set_analytics(self, sensor):
        self.analytics_sensor = sensor

    def stitch_images(self):
        stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
        (status, self.stitched) = stitcher.stitch(self.images)
        if status == 0:
            # write the output stitched image to file
            cv2.imwrite(self.output_dir, self.stitched)
            if self.analytics_sensor is not None:
                self.analytics_sensor.mask_images()

        # otherwise the stitching failed, likely due to not enough keypoints)
        # being detected
        else:
            print("[INFO] image stitching failed ({})".format(status))
