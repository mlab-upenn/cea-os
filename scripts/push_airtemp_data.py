"""
This is a script to push air temperature data to InfluxDB
Originally written as a test on the RPi (home/pi) with physical sensor
"""
from ceaos.sensors.temperature_sensor import Temperature
from ceaos.loggers.InfluxDB import InfluxDBConnection, InfluxDBLogger

# import os
# import sys
# os.chdir('pigpio_dht22')
# sys.path.append("/home/pi/pigpio_dht22")
import pigpio
import DHT22

pi = pigpio.pi()
s = DHT22.sensor(pi, 4)
s.trigger()
s.trigger()


# Get temperature reading from physical sensor
def get_temp(phys_sensor: DHT22):  # what datatype is phys_sensor?
    if (phys_sensor.humidity() is not None
            and phys_sensor.temperature() is not None):
        newTemp = phys_sensor.temperature()
    else:
        newTemp = None
        print("Error: sensor read failed")
    return newTemp


newTemp = get_temp(s)
while newTemp == -999.0:
    newTemp = get_temp(s)

# Make temp sensor with newTemp
airTemp = Temperature(newTemp, "Air_Temp")
print(airTemp.read_value())

# Make a logger
aConnection = InfluxDBConnection()
aConnection.configure()
tempLogger = InfluxDBLogger(airTemp)

# Send off data
tempLogger.send_logs("Environment", "lettuce",
                     airTemp.get_datatype(), aConnection)
