from ceaos.sensors import sensor_definition
from ceaos.sensors.artificial_sensor import Artificial_Sensor
from ceaos.loggers.InfluxDB import InfluxDBConnection
from ceaos.loggers.InfluxDB import InfluxDBLogger
from ceaos.objects.farm import Farm
from ceaos.objects.environment import Environment
from ceaos.objects.beds import Bed
from ceaos.objects.plants import Plant
from ceaos.cfg import load_config

import time
import threading
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

'''
Data logging function
'''
def log_data(refresh_rate,logger_list, client, farm_name):
	try:
		while True:
			for logger in logger_list:
				logger.send_logs(farm_name, logger.get_sensor().get_datatype(),
								 logger.get_location(), client)
				time.sleep(refresh_rate)
	except KeyboardInterrupt:
		logging.info("Logger ended")

if __name__ == "__main__":
	farm, sensors, db_client, error = load_config("config.yaml")	#Set up Farm from config file
	if error != None or farm == None:
		logging.error(error)
		quit()
	loggers = {}	#Dictionary of loggers (key = refresh_rate, value = list of loggers)

	time.sleep(5)
	
	
	db_client = InfluxDBConnection()	#Set up InfluxDB Client
	db_client.configure()
	logging.info("DB Client Configured")
	
	farm_name = farm.get_name()

	for sensor in sensors:
		refresh_rate = sensor.get_refresh()
		logger = InfluxDBLogger(sensor)
		sensor.set_logger(logger)
		logger.set_location(sensor.get_location())
		logger.set_refresh_rate(refresh_rate)
		if refresh_rate not in loggers:
			loggers[refresh_rate] = [logger]
		else:
			loggers.get(refresh_rate).append(logger)

	logging.info("Loggers created for sensors")
	threads = []

	for refresh_rate, logger_list in loggers.items():
		thread = threading.Thread(target=log_data, args=(refresh_rate, logger_list, db_client, farm_name))
		threads.append(thread)
	
	logging.info("Logging threads created")

	for thread in threads:
		thread.start()
	
	logging.info("Logging threads started")

	for thread in threads:
		thread.join()

	logging.info("Logging threads joined. Terminating")
