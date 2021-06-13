#################################
# CEA-OS
# Load CSV data to InfluxDB
# Author: Sarah Santos
# Created: 6/1/2021
#################################

# ==================== 0. Import needed packages
import pandas as pd
import xlrd
import time  # I don't think I acutally use this..
from datetime import tzinfo, timedelta, datetime
from influxdb import InfluxDBClient

# ==================== I. Set up client
# ----- A. InfluxDB connection
client = InfluxDBClient(host="localhost", port=8086, username="grafana", password="password")

client.create_database("CEAOD_AiCU")
client.switch_database("CEAOD_AiCU")

# ----- B. TZ Class for time entry
class TZ(tzinfo):  # class needed to clean up time entry later
    def utcoffset(self, dt):
        return timedelta(minutes=-399)


# ==================== II. Load Irrigation.csv

# ----- A. Set up file path
irrigationFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/Irrigation/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/Irrigation.csv"
irrgationData = pd.read_csv(irrigationFilePath)
# print(csvReader.shape)
# print(csvReader.columns)


# ----- B. Iterate through to read in data
json_irrigation = []

for row_index, row in irrgationData.iterrows():
    ECDrainValue = row[0]
    drainValue = row[1]
    pHDrainValue = row[2]
    waterValue = row[4]
    #### convert time value from XL to Python datetime then to JSON protocol
    xl_date = row[3]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(
        date_object.year, date_object.month, date_object.day, tzinfo=TZ()
    ).isoformat()
    # print(timeValue)
    data = {
        "measurement": "Irrigation",
        # "tags": {
        #     },
        "time": timeValue,
        "fields": {
            "EC_Drain": ECDrainValue,
            "drain": drainValue,
            "pH_Drain": pHDrainValue,
            "water": waterValue,
        },
    }
    json_irrigation.append(data)
    # print(data)

# ----- C. Write data to InfluxDB
client.write_points(json_irrigation)


# ==================== III. Load Production.csv

# ----- A. Set up file path
productionFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/Production/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/Production.csv"
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
    #### convert time value from XL to Python datetime
    xl_date = row[6]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(
        date_object.year, date_object.month, date_object.day, tzinfo=TZ()
    ).isoformat()
    # print(timeValue)
    data = {
        "measurement": "Production",
        # "tags": {
        #     },
        "time": timeValue,
        "fields": {
            "ProdA_cum": ProdA_cum,
            "ProdA_num": ProdA_num,
            "ProdB_cum": ProdB_cum,
            "ProdB_num": ProdB_num,
            "Prod_value_cum": Prod_value_cum,
            "Total_Prod_cum": Total_Prod_cum,
        },
    }
    json_production.append(data)
    # print(data)

# ----- C. Write data to InfluxDB
client.write_points(json_production)


# ==================== IV. Load Greenhouse_climate.csv

# ----- A. Set up file path
greenhouseFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/Greenhouse_climate/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/Greenhouse_climate.csv"
greenhouseData = pd.read_csv(greenhouseFilePath)

# ----- B. Iterate through to read in data
json_greenhouse = []

for row_index, row in greenhouseData.iterrows():
    AssimLight = row[0]
    BlackScr = row[1]
    CO2air = row[2]
    EnScr = row[3]
    HumDef = row[5]
    PipeGrow = row[6]
    PipeLow = row[7]
    RHair = row[8]
    Tair = row[9]
    VentLee = row[10]
    Ventwind = row[11]
    #### convert time value from XL to Python datetime
    xl_date = row[4]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(
        date_object.year, date_object.month, date_object.day, tzinfo=TZ()
    ).isoformat()
    #print(timeValue)
    data = {
        "measurement": "Greenhouse_climate",
        # "tags": {
        #     },
        "time": timeValue,
        "fields": {
            "AssimLight": AssimLight,
            "BlackScr": BlackScr,
            "CO2air": CO2air,
            "EnScr": EnScr,
            "HumDef": HumDef,
            "PipeGrow": PipeGrow,
            "PipeLow": PipeLow,
            "RHair": RHair,
            "Tair": Tair,
            "VentLee": VentLee,
            "Ventwind": Ventwind,
        },
    }
    json_greenhouse.append(data)
    # print(data)

# ----- C. Write data to InfluxDB
client.write_points(json_greenhouse)


# ==================== IV. Load ResourceCalculations.csv

# ----- A. Set up file path
resourceCalcFilePath = "C:/Users/sarah/Dropbox/IoT4Ag/CEAOD/ResourceCalculations/GH_Cucumber/AutonomousGreenhouseChallenge2018/AiCU/ResourceCalculations.csv"
resourceCalcData = pd.read_csv(resourceCalcFilePath)

# ----- B. Iterate through to read in data
json_resourceCalc = []

for row_index, row in resourceCalcData.iterrows():
    CO2_dosage = row[0]
    Electricity_Lamp = row[1]
    Heating_Energy = row[2]
    Labour = row[3]
    net_water = row[4]
    #time_ = row[5]
    #### convert time value from XL to Python datetime
    xl_date = row[5]
    datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
    date_object = datetime_date.date()
    # print(date_object)
    timeValue = datetime(
        date_object.year, date_object.month, date_object.day, tzinfo=TZ()
    ).isoformat()
    #print(timeValue)
    data = {
        "measurement": "ResourceCalculations",
        # "tags": {
        #     },
        "time": timeValue,
        "fields": {
            'CO2_dosage': CO2_dosage,
            'Electricity_Lamp': Electricity_Lamp,
            'Heating_Energy': Heating_Energy,
            'Labour': Labour,
            'net_water': net_water,
        },
    }
    json_resourceCalc.append(data)
    # print(data)

# ----- C. Write data to InfluxDB
client.write_points(json_resourceCalc)
