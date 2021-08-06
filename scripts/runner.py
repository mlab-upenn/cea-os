from ceaos.sensors.nwsensor import NetworkSensor
from ceaos.loggers.InfluxDB import InfluxDBConnection
from ceaos.loggers.InfluxDB import InfluxDBLogger
from ceaos.cfg import load_config
from ceaos.api import create_api
from ceaos.grow import load_grow

import time
import threading
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
"""
Data logging function
"""


def log_data(refresh_rate, logger_list, client):
    try:
        while True:
            for logger in logger_list:
                logger.send_logs("sensor_data",
                                 logger.get_sensor().get_datatype(),
                                 logger.get_location(), client)
                time.sleep(refresh_rate)
    except:
        print(refresh_rate)
        logging.info("Logger ended")


if __name__ == "__main__":
    farm, sensors, actuators, connection_dict, error = load_config(
        "ceaos.resources", "config.yaml")  # Set up Farm from config file
    if error is not None or farm is None:
        logging.error(error)
        quit()
    loggers = {
    }  # Dictionary of loggers (key = refresh_rate, value = list of loggers)

    time.sleep(5)

    db_client = InfluxDBConnection()
    db_client.configure(
        host=connection_dict.get("host"),
        port=connection_dict.get("port"),
        username=connection_dict.get("username"),
        password=connection_dict.get("password"),
        database=connection_dict.get("database"),
    )

    logging.info("DB Client Configured")
    farm_name = farm.get_name()

    # this is a list of lists
    recipe_list = []
    directory = "cea-os/ceaos/resources/config/recipes"

    for recipe in os.scandir(directory):
        recipe_to_add = load_grow(directory, recipe)
        recipe_list.append(recipe_to_add)

    print(recipe_list)

    for sensor in sensors:  # NetworkSensors will have a refresh rate of None
        logger = InfluxDBLogger(sensor)
        logger.set_location(sensor.get_location())
        sensor.set_logger(logger)
        if isinstance(sensor, NetworkSensor):
            sensor.set_influxconnection(db_client)
        elif not isinstance(sensor, NetworkSensor):
            refresh_rate = sensor.get_refresh()
            logger.set_refresh_rate(refresh_rate)

        if logger.get_refresh_rate() is not None:
            if logger.get_refresh_rate() not in loggers:
                loggers[refresh_rate] = [logger]
            else:
                loggers.get(refresh_rate).append(logger)

    logging.info("Loggers created for sensors")
    threads = []

    for refresh_rate, logger_list in loggers.items():
        thread = threading.Thread(
            target=log_data,
            args=(refresh_rate, logger_list, db_client),
            daemon=True,
        )
        threads.append(thread)

    logging.info("Logging threads created, Threads: %d ", len(threads))

    threads.append(
        threading.Thread(target=create_api, args=(farm, ), daemon=True))

    logging.info("API Thread created")

    threads.append(threading.Thread(target=create_api, args=(farm,), daemon=True))

    logging.info("API Thread created")

    for thread in threads:
        thread.start()

    logging.info("Logging/API threads started")

    for thread in threads:
        thread.join()

    logging.info("Logging/API threads joined. Terminating")
