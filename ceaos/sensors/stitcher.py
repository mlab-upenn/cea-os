# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
from .image_analysis_sensor import *

class Stitcher():
    def __init__(self):
        self.stitched = None
        self.output_path = './images/stitched.png'

    def stitch_images(self, images):
        stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
        (status, self.stitched) = stitcher.stitch(images)
        if status == 0:
            # write the output stitched image to file
            cv2.imwrite(self.output_path, self.stitched)
            return self.output_path

        # otherwise the stitching failed (likely due to not enough keypoints)
        # being detected
        else:
            print("[INFO] image stitching failed ({})".format(status))
            return None
