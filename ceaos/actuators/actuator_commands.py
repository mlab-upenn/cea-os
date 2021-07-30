from ..objects import Farm, Environment, Bed
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def set_pH(ip, max, min):
    logging.info("set pH")

def set_EC(ip, max, min):
    logging.info("set EC")

def set_lights(ip, max, min):
    logging.info("set Lights")

def set_airtemp(ip, max, min):
    logging.info("set air temp")

def set_camera(ip):
    logging.info("set camera")
