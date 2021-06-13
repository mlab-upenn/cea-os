#################################
# CEA-OS
# Load CSV data to InfluxDB
# Author: Sarah Santos
# Created: 6/1/2021
#################################

# ==================== 0. Import needed packages
import pandas as pd
import xlrd
from datetime import tzinfo, timedelta, datetime
from influxdb import InfluxDBClient

# ==================== I. Set up client
client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='password')

client.create_database('CEAOD_AiCU')
client.switch_database('CEAOD_AiCU')

# ==================== II. Load Irrigation.csv

# ----- A. Set up file path
irrigationFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/Irrigation/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/Irrigation.csv"  # noqa: E501
irrgationData = pd.read_csv(irrigationFilePath)
# print(csvReader.shape)
# print(csvReader.columns)

# ----- B. TZ Class for time entry


class TZ(tzinfo):  # class needed to clean up time entry later
    def utcoffset(self, dt): return timedelta(minutes=-399)


# ----- C. Iterate through to read in data
json_irrigation = []

for row_index, row in irrgationData.iterrows():
    ECDrainValue = row[0]
    drainValue = row[1]
    pHDrainValue = row[2]
    waterValue = row[4]
    # convert time value from XL to Python datetime then to JSON protocol
    xl_date = row[3]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(date_object.year, date_object.month, date_object.day, tzinfo=TZ()).isoformat()
    # print(timeValue)
    data = {
        "measurement": "Irrigation",
        # "tags": {

        #     },
        "time": timeValue,
        "fields": {
            'EC_Drain': ECDrainValue,
            'drain': drainValue,
            'pH_Drain': pHDrainValue,
            'water': waterValue
        }
    }
    json_irrigation.append(data)
    # print(data)

# ----- D. Write data to InfluxDB
client.write_points(json_irrigation)


# ==================== III. Load Production.csv

# ----- A. Set up file path
productionFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/Production/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/Production.csv"  # noqa: E501
productionData = pd.read_csv(productionFilePath)

# ----- B. Iterate through to read in data
json_production = []

for row_index, row in productionData.iterrows():
    ProdA_cum = row[0]
    ProdA_num = row[1]
    ProdB_cum = row[2]
    ProdB_num = row[3]
    Prod_value_cum = row[4]
    Total_Prod_cum = row[5]
    # convert time value from XL to Python datetime
    xl_date = row[6]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(date_object.year, date_object.month, date_object.day, tzinfo=TZ()).isoformat()
    # print(timeValue)
    data = {
        "measurement": "Production",
        # "tags": {

        #     },
        "time": timeValue,
        "fields": {
            'ProdA_cum': ProdA_cum,
            'ProdA_num': ProdA_num,
            'ProdB_cum': ProdB_cum,
            'ProdB_num': ProdB_num,
            'Prod_value_cum': Prod_value_cum,
            'Total_Prod_cum': Total_Prod_cum
        }
    }
    json_production.append(data)
    # print(data)

# ----- D. Write data to InfluxDB
client.write_points(json_production)
