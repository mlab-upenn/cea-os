from ceaos.loggers.InfluxDB import InfluxDBConnection, InfluxDBLogger
import pytest
from ceaos.sensors.nwsensor import NetworkSensor


def setup_sensor() -> NetworkSensor:
    logger = InfluxDBLogger()
    return NetworkSensor(logger)


def test_creation():
    logger = InfluxDBLogger()
    NetworkSensor(logger)


def test_recv():
    a = setup_sensor()
    assert ((a.recv_value(ph=7, ec=180, watertemp=50)) == 'Successful Connection to Network Sensor')


def test_read():
    a = setup_sensor()
    a.recv_value(5)
    assert (a.read_value()) == 5

def test_read2():
    a = setup_sensor()
    a.recv_value(ph=7, ec=180, watertemp=50)
    assert (a.read_value() == {"ph":7, "ec":180, "watertemp":50})
