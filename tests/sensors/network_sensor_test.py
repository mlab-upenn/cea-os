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
    connect = InfluxDBConnection()
    assert ((a.recv_value(5, connect)) == "successfully logged and updated")


def test_read():
    a = setup_sensor()
    connect = InfluxDBConnection()
    a.recv_value(5, connect)
    assert (a.read_value() == 5)
    