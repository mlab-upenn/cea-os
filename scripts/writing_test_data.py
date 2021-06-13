# CEA-OS
# Test writing data to InfluxDB from Python
# Author: Brad Morg (from GitHub)
# Modified by: Sarah Santos
# Modified on: 6/1/2021

# ##### Import the stuff we need
# pip install influxdb
from rich import print
from influxdb import InfluxDBClient
from datetime import datetime
from datetime import timedelta  # idk what i'm doing here, but trying to debug timedelta issues

# ##### Setup database
client = InfluxDBClient(
    host='localhost', port=8086, username='grafana',
    password='password')  # username credentials from docker-compose.yml file
# client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='password', database='grafana')

client.create_database(
    'testdb'
)  # the Compose file automatically makes a database named "grafana", but I make another one for testing
# client.get_list_database() # view all databases
client.switch_database('testdb')  # work in 'testdb'

# ##### Setup Payload
# made a few more datapoints
json_payload = []
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "tomatoes"
    },
    "time": datetime.now() - timedelta(minutes=10),
    "fields": {
        'pH': 5.7,
        'EC': 3.3
    }
}
json_payload.append(data)
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "tomatoes"
    },
    "time": datetime.now(),
    "fields": {
        'pH': 6.0,
        'EC': 3.5
    }
}
json_payload.append(data)
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "lettuce"
    },
    "time": datetime.now() - timedelta(minutes=10),
    "fields": {
        'pH': 5.9,
        'EC': 1.1
    }
}
json_payload.append(data)
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "lettuce"
    },
    "time": datetime.now(),
    "fields": {
        'pH': 6.1,
        'EC': 0.9
    }
}
json_payload.append(data)
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "strawberries"
    },
    "time": datetime.now() - timedelta(minutes=10),
    "fields": {
        'pH': 6.1,
        'EC': 0.9
    }
}
json_payload.append(data)
data = {
    "measurement": "NutrientSolution",
    "tags": {
        "plant": "strawberries"
    },
    "time": datetime.now(),
    "fields": {
        'pH': 5.7,
        'EC': 0.8
    }
}
json_payload.append(data)

# ##### Send our payload
client.write_points(json_payload)

# ##### Select statement
# # It was more helpful for me to query the database from the InfluxDB container CLI
# need to install "rich" first..
# print(data)
result = client.query('select * from NutrientSolution;')
print(result)
