#!/usr/bin/python
import os
import pymysql
import sys
import json
import requests
from flask import Flask, request
from datetime import date
from datetime import datetime
import cgi
import cgitb
from random import seed
from random import randint
cgitb.enable()

print("Content-Type: text/html")
print("")

server_name = 'localhost'
username = 'iotdev'
password = 'iotdb190'
dbname = 'iotdb'

#create connection
connection = pymysql.connect(
    host= server_name, 
    user=username, 
    password=password,
    db=dbname,
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
    )

cursor = connection.cursor()
def update_sd():
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=32.72&lon=-117.16&exclude=minutely,hourly,daily&appid=0354c29c5e773c46d37727c8a0455d58'
    params = {'lat': 32.72, 'lat': -117.16, 'exclude':'minutely','appid': "0354c29c5e773c46d37727c8a0455d58"}
    r = requests.get(url)
    data = r.json()
    timestamp = datetime.now()
    lon = data['lon']
    lat = data['lat']
    city = 'San Diego'
    wind_speed = data['current']['wind_speed']
    wind_deg = data['current']['wind_deg']
    cloudiness = data['current']['clouds']

    sql = "INSERT INTO weather(lon, lat, city, wind_speed, wind_deg, cloudiness, time) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (lon, lat, city, wind_speed, wind_deg, cloudiness, timestamp)
    cursor.execute(sql)
    print('executed')

def update_bay():
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=37.3382&lon=-121.8863&exclude=minutely,hourly,daily&appid=0354c29c5e773c46d37727c8a0455d58'
    #params = {'lat': 32.72, 'lat': -117.16, 'exclude':'minutely','appid': "0354c29c5e773c46d37727c8a0455d58"}
    r = requests.get(url)
    data = r.json()
    timestamp = datetime.now()
    lon = data['lon']
    lat = data['lat']
    city = 'San Jose'
    wind_speed = data['current']['wind_speed']
    wind_deg = data['current']['wind_deg']
    cloudiness = data['current']['clouds']

    sql = "INSERT INTO weather(lon, lat, city, wind_speed, wind_deg, cloudiness, time) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (lon, lat, city, wind_speed, wind_deg, cloudiness, timestamp)
    cursor.execute(sql)
    print('executed')


def update(lat, lon, area, devmac):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,hourly,daily&appid=0354c29c5e773c46d37727c8a0455d58' % (lat, lon)
    r = requests.get(url)
    data = r.json()
    timestamp = datetime.now()
    lon = lon
    lat = lat
    city = area
    wind_speed = data['current']['wind_speed']
    wind_deg = data['current']['wind_deg']
    cloudiness = data['current']['clouds']
    mac = devmac

    sql = "INSERT INTO weather(lon, lat, city, wind_speed, wind_deg, cloudiness, time, devmac) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (lon, lat, city, wind_speed, wind_deg, cloudiness, timestamp, mac)
    cursor.execute(sql)

import time
starttime=time.time()
while True:
    update(32.9269, -117.195, 'Group 1 San Diego', 'CC:50:E3:AF:E1:B4')
    update(32.8512, -117.217, 'Group 22 San Diego', '3C:71:BF:63:DC:D0')
    update(32.8741, -117.218, 'Group 10 San Diego', '3C:71:BF:6C:A9:7C')
    update(32.856, -117.212, 'Group 5 San Diego', 'CC:50:E3:A8:EB:3C')
    update(32.8472, -117.196, 'Group 2 San Diego', '3C:71:BF:64:36:C0')
    update(37.3969, -121.943, 'Group 2 Bay', '3C:71:BF:6C:62:2C')
    update(32.8711, -117.217, 'Group 11 San Diego', '80:7D:3A:E9:67:5C')
    update(32.869, -117.218, 'Group 11 San Diego', '3C:71:BF:62:E7:FC')
    update(32.869, -117.218, 'Group 22 San Diego', 'CC:50:E3:B0:92:B4')
    update(32.8725, -117.205, 'Group 9 San Diego', 'CC:50:E3:B0:21:78')
    update(32.8697, -117.223, 'Group 20 San Diego', 'CC:50:E3:A1:45:2C')
    update(32.8657, -117.238, 'Group 3 San Diego', '80:7D:3A:BA:E2:14')
    update(37.7833, -122.287, 'Group 18 Bay', 'CC:50:E3:AF:E4:68')
    update(37.4918, -121.925, 'Group 18 Bay', 'A4:CF:12:43:71:60')
    update(32.8747, -117.216, 'Group 6 San Diego', '3C:71:BF:6C:5D:B4')
    update(32.8668, -117.248, 'Group 3 San Diego', '3C:71:BF:63:81:BC')
    update(32.8746, -117.216, 'Group 6 San Diego', 'A4:CF:12:43:71:4C')
    update(37.3877, -122.007, 'Group 4 Bay', 'CC:50:E3:AF:E3:80')
    update(37.7423, -122.259, 'Group 12 Bay', 'A4:CF:12:43:52:D0')
    update(32.8584, -117.233, 'Group 12 San Diego', 'CC:50:E3:A9:79:3C')
    update(37.7124, -122.421, 'Group 14 Bay', '3C:71:BF:63:E6:30')
    update(37.3688, -122.036, 'Group 1 Bay', '3C:71:BF:6F:13:B8')

    #LA
    update(33.705, -117.738, 'Group 15 LA', 'CC:50:E3:B0:21:A4')
    update(33.6962, -117.79, 'Group 25 LA', '3C:71:BF:62:E4:30')
    update(33.7947, -118.397, 'Group 25 LA', '3C:71:BF:64:21:DC')
    update(33.8647, -118.267, 'Group 13 LA', 'CC:50:E3:AF:E4:E0')
    update(34.1542, -118.045, 'Group 16 LA', '3C:71:BF:63:EE:0C')
    update(34.2192, -118.352, 'Group 5 LA', 'CC:50:E3:B0:21:8C')
    
    time.sleep(3600)
