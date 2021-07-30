import json
import zmq
from ..objects import Farm, Environment, Bed

def set_pH(ip, max, min, socket):
    print("set pH")
    socket.send_string("ph set")

def set_EC(ip, max, min, socket):
    print("set EC")
    socket.send_string("ec set")

def set_lights(ip, max, min, socket):
    print("set Lights")
    socket.send_string("light set")

def set_airtemp(ip, max, min, socket):
    print("set airtemp")
    socket.send_string("air set")

def set_camera(ip, socket):
    print("set camera")
    socket.send_string("cam set")