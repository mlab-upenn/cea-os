from ..loggers.InfluxDB import InfluxDBConnection, InfluxDBLogger
from .sensor_definition import Sensor
from plantcv import plantcv as pcv
import base64
import datetime
import numpy as np
import json
import os
from ..objects.beds import *
from .stitcher import *

class ImageAnalyticsSensor(Sensor):
    def __init__(self, db_client: InfluxDBConnection) -> None:
        self.images = None
        self.image_data = None
        self.images_folder = './images/RGB_orig/'
        self.masks_folder = './images/masks/'
        self.plant_img_folder = './images/plants/'
        self.client = db_client
        self.logger = InfluxDBLogger(sensor = self)
        self.measurements = './images/measurements/measurements.json'
        self.location = None    # String
        self.cameras = []
        self.stitcher = Stitcher()
        self.plant_names = []

    def read_value(self, database_name: str, num_images: int, field: str, location: str):
        return self.image_data

    def calibrate(self):
        print("Camera calibration must be done manually by the user")

    def set_location(self, location):
        self.location = location

    def query_db(self, database_name:str, num_images: int, field: str):
        results = self.client.query(f"""SELECT * FROM "{database_name}"."autogen"."{field}" 
        GROUP BY * ORDER BY DESC LIMIT {str(num_images)}""")
        self.images = results.get_points(tags = {'location': self.location})

    def stitch_images(self, images):
        output_path = self.stitcher.stitch_images(images)    # Stitches image and returns output dir if successful, else None
        if output_path is not None:
            with open(output_path, 'rb') as imagefile:
                self.image_data = base64.b64encode(imagefile.read())    # Encode stitched image and send to database
            self.logger.send_logs("analysis", "stitched_image", self.location, self.client.get_connection())
            self.images = self.image_data   # Set images attribute to encoded stitched image for masking function
            os.remove(output_path)
            return True
        else:
            return False


    def mask_images(self):
        # Decode images
        now = datetime.now()
        date_str = now.strftime("__%Y_%m_%d__%H:%M")
        image_name = self.location + date_str + ".png"
        self.decode_image(self.images, self.images_folder + image_name) # Saves decoded image in temporary image folder
    
        # Read image
        img, path, filename = pcv.readimage(filename= self.images_folder + image_name)

        img = pcv.white_balance(img, mode = 'hist')

        # Convert RGB to LAB and extract the Blue channel
        
        b = pcv.rgb2gray_lab(rgb_img=img, channel='l')

        # Threshold the lightness image
        b_thresh = pcv.threshold.binary(gray_img=b, threshold=95, max_value=255, 
                                        object_type='light')

        # Fill small objects (optional)
        b_fill = pcv.fill(b_thresh, 200)

        #Apply a mask
        masked = pcv.apply_mask(img=img, mask=b_fill, mask_color = 'white')
        
        mask_green, masked_image = pcv.threshold.custom_range(img=masked, lower_thresh=[10,100,10], upper_thresh=[252,255,252], channel='RGB')
        g_fill = pcv.fill(mask_green, 800)
        g_mblur = pcv.median_blur(gray_img = g_fill, ksize = 20)
        masked_image = pcv.apply_mask(img = img, mask = g_mblur, mask_color = 'white')

        # Convert RGB to LAB and extract the Green-Magenta channel
        masked_a = pcv.rgb2gray_lab(rgb_img=masked_image, channel='a')

        # Threshold the green-magenta image
        maskeda_thresh = pcv.threshold.binary(gray_img=masked_a, threshold=125, 
                                        max_value=255, object_type='dark')
        
        b_mblur = pcv.median_blur(gray_img=maskeda_thresh, ksize=15)
        ab_fill = pcv.fill(bin_img= b_mblur, size=500)

        # Apply mask (for VIS images, mask_color=white)
        masked2 = pcv.apply_mask(img=masked, mask=ab_fill, mask_color='white')

        id_objects, obj_hierarchy = pcv.find_objects(img, ab_fill)

        roi1, roi_hierarchy= pcv.roi.rectangle(img=masked2, x=115, y=140, h=2500, w=3500)

        roi_objects, hierarchy3, kept_mask, obj_area = pcv.roi_objects(img=img, roi_contour=roi1, 
                                                                    roi_hierarchy=roi_hierarchy, 
                                                                    object_contour=id_objects, 
                                                                    obj_hierarchy=obj_hierarchy,
                                                                    roi_type='partial')
        mask_name = image_name[:-4]
        mask_name += "_mask.jpg"

        # Save mask image
        pcv.print_image(kept_mask, self.masks_folder + mask_name)

        # Encode and upload mask image to database
        with open(self.masks_folder + mask_name, 'rb') as imagefile:
            self.image_data = base64.b64encode(imagefile.read())
        self.logger.send_logs("analysis", "mask_images", self.location, self.client.get_connection())
        os.remove(self.masks_folder + mask_name)
        
        #CHANGE THESE COORDINATES
        rois1, roi_hierarchy1 = pcv.roi.multi(img=img, coord=[(650,750), (1880,800), (3260,850), (700, 2080), (1960,2100), (3350, 2150)], radius=600)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        img_copy = np.copy(img)

        #Check if number of plants detected is same as number of plant names given
        if len(self.plant_names) == len(rois1):
            use_names = True
        else:
            use_names = False

        # Analyze each plant using the ROI's created by using the grid setup for pcv.roi.multi
        for i in range(0, len(rois1)):
            if use_names:
                plant_image_name = f"{self.location}_{self.plant_names[i]}{date_str}.jpg"
            else:
                plant_image_name = f"{self.location}_plant{i}{date_str}.jpg"
            roi = rois1[i]
            hierarchy = roi_hierarchy1[i]
            # Filter objects by ROI 
            filtered_contours, filtered_hierarchy, filtered_mask, filtered_area = pcv.roi_objects(
                img=img, roi_type="partial", roi_contour=roi, roi_hierarchy=hierarchy, object_contour=roi_objects, 
                obj_hierarchy=hierarchy3)

            # Combine objects together in each plant     
            plant_contour, plant_mask = pcv.object_composition(img=img_copy, contours=filtered_contours, hierarchy=filtered_hierarchy)        

            # Analyze the shape of each plant 
            img_copy = pcv.analyze_object(img=img_copy, obj=plant_contour, mask=plant_mask, label="plant" + str(i))
            
            #Crop plants based on contours
            cropped = pcv.auto_crop(img = img, obj = plant_contour, padding_x=500, padding_y=500, color='image')
            
            # Save individual plant images to database
            pcv.print_image(cropped, self.plant_img_folder + plant_image_name)
            with open(self.plant_img_folder + plant_image_name, 'rb') as imagefile:
                self.image_data = base64.b64encode(imagefile.read())

            if use_names:
                self.logger.send_logs("sensor_data", "indiv_images", f"{self.location}.{self.plant_names[i]}", self.client.get_connection())
            else:
                self.logger.send_logs("sensor_data", "indiv_images", f"{self.location}.plant{i}", self.client.get_connection())
            
            os.remove(self.plant_img_folder + plant_image_name)

        # Save data on plant shape to json file
        pcv.outputs.save_results(filename=self.measurements)

    def log_area(self):
        f = open(self.measurements)
        data = json.load(f)
        plants = list(data['observations'].keys())
        for i in range(plants):
            self.image_data = data['observations'][plants[i]]['area']['value']
            self.logger.send_logs("analysis", "leaf_area", f"{self.location}.{plants[i]}", self.client.get_connection())
        os.remove(self.measurements)

    def decode_image(self, encoded_data: str, image_name: str):   # Decode Base64 encoded image stored as string in DB
        data = encoded_data.encode('ascii')
        with open(image_name, "wb") as fh:
            fh.write(base64.decodebytes(data))

    def analyze(self):
        self.query_db('grafana', len(self.cameras), self.camera[0].get_datatype())  # Pulls most recent images from db for every associated camera
        if self.stitch_images(self.images): # Stitches images
            self.mask_images()  # If stitching is successful, mask and crop the images
            self.log_area() # Record the leaf area in the database
        else:
            print("ERROR: Image stitching failed")


