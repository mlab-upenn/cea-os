"""
This is a test file to pushe air temperature data to InfluxDB
Originally written as a test on the RPi
"""
from ceaos.sensors.temperature_sensor import Temperature

### Test import - it works for me locally, but when I ran this on the Pi I had all the needed modules in the same directory
# airTemp = Temperature()
# print(airTemp.read_value())

#### COPYING CODE FROM temp_sens.py - ADJUST imports accordingly!
import os
import sys
import time
os.chdir('pigpio_dht22')
sys.path.append("/home/pi/pigpio_dht22")
import pigpio
pi = pigpio.pi()
import DHT22
s = DHT22.sensor(pi, 4)
s.trigger()
s.trigger()
#### END OF COPIED CODE

## Get temperature reading from physical sensor
def get_temp(phys_sensor: DHT22): #what datatype is phys_sensor? what does DHT22.sensor() return
    if phys_sensor.humidity() != None and phys_sensor.temperature() != None:
        newTemp = phys_sensor.temperature()
    else:
        newTemp = None
        print('Error: sensor read failed')
    return newTemp
    
newTemp = get_temp(s)
while (newTemp == -999.0): #
    newTemp = get_temp(s)

## Make temp sensor with newTemp
airTemp = Temperature(newTemp, "Air_Temp")
print(airTemp.read_value())

## Make a logger
aConnection = InfluxDBConnection()
aConnection.configure()
tempLogger = InfluxDBLogger(airTemp)

## Send off data
tempLogger.send_logs("Environment", "lettuce", airTemp.get_datatype(), aConnection)