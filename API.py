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
import random
from random import seed
from random import randint
import numpy as np
import math
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

#POST Interface

inputs = json.load(sys.stdin)
params = {}
for key, value in inputs.items():
    key = str(key)
    value = str(value)
    params[key] = value
command = params['cmd']

import ast

np.random.seed(42)

post = True

if post:

    if "WIND_HEATMAP" in command:
        if "-" in command[-2:]:
            sql = "SELECT devmac, lat, lon, wind_speed FROM weather where entry in (SELECT max(entry) FROM weather WHERE time < DATE_SUB(now(), INTERVAL %s DAY) group by devmac) and devmac is not null" % (eval(command[-1:]))

        if command[-1:] in ["1","2","3"]:
            sql = "SELECT max(lat) lat, max(lon) lon, devmac, '%s'*avg(wind_speed) wind_speed FROM weather group by devmac" % math.sqrt(math.sqrt(eval(command[-1:])))

        if command[-1:] == "0":
            sql = "SELECT devmac, lat, lon, wind_speed FROM weather where entry in (SELECT max(entry) FROM weather group by devmac) and devmac is not null"
        
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            row['COORDINATES'] = [row['lon'], row['lat']]
            row['wind_speed'] = row['wind_speed']
        data = str(rows).replace("u\'",'\'').replace("'",'"').replace('wind_speed', 'WEIGHT')
        print(data)


    if "HEXAGON" in command:
        if "-" in command[-2:]:
            sql = "SELECT timerstamp, hum, dev_lat, dev_long FROM iotdb.mcdata, iotdb.devices where id in (SELECT max(id) FROM iotdb.mcdata WHERE timerstamp < DATE_SUB(now(), INTERVAL '%s' DAY) group by mac) and iotdb.mcdata.mac = iotdb.devices.mac and iotdb.devices.dev_lat is not null" % (eval(command[-1:]))
        
        if command[-1:] in ["1","2","3"]:
            sql = "SELECT devices.mac, '%s'*avg(hum) hum, max(dev_lat) dev_lat, max(dev_long) dev_long FROM iotdb.mcdata, iotdb.devices where id in (SELECT max(id) FROM iotdb.mcdata group by mac) and iotdb.mcdata.mac = iotdb.devices.mac and iotdb.devices.dev_lat is not null group by devices.mac" % math.sqrt(math.sqrt(eval(command[-1:])))
        
        if command[-1:] == "0":
            sql = "SELECT hum, dev_lat, dev_long FROM mcdata, devices where id in (SELECT max(id) FROM mcdata group by mac) and mcdata.mac = devices.mac and devices.dev_lat is not null;"

        data = []
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = []

        #San Diego
        sd_lon = [random.uniform(-117.0, -117.3) for i in range(200)]
        sd_lat = [random.uniform(32.7, 33) for i in range(200)]
        hum = [1]*200

        #San Jose
        sj_lon = [random.uniform(-121.7, -122.1) for i in range(200)]
        sj_lat = [random.uniform(37.15, 37.55) for i in range(200)]

        #LA
        la_lon = [random.uniform(-117.9, -118.65) for i in range(400)]
        la_lat = [random.uniform(33.7, 34.3) for i in range(400)]
        la_hum = [1]*400

        sd_noise = list(map(list, zip(sd_lat, sd_lon, hum)))
        sj_noise = list(map(list, zip(sj_lat, sj_lon, hum)))
        la_noise = list(map(list, zip(la_lat, la_lon, la_hum)))

        for row in rows:
            newrows.append([row['dev_lat'], row['dev_long'], 3*int(row['hum'])])

        newrows = newrows + sd_noise + sj_noise + la_noise
        data = str(newrows).replace("u\'",'\'').replace("'",'"')
        print(data)
    
    if command == "CURRENT_WEATHER":
        devmac = params['devmac']
        data = []
        sql_mc = "select temp, hum from mcdata where mac = '%s' order by timerstamp desc limit 1" % devmac
        cursor.execute(sql_mc)
        rows = cursor.fetchall()[0]
        data.append(rows['temp'])
        data.append(rows['hum'])

        sql_weather = "select city, wind_speed, wind_deg, cloudiness from weather where devmac = '%s' order by time desc limit 1" % devmac
        cursor.execute(sql_weather)
        rows = cursor.fetchall()[0]
        data.append(eval(rows['wind_speed']))
        data.append(eval(rows['wind_deg'])) 
        data.append(eval(rows['cloudiness'])) 
        data.append(rows['city'])
        data = [data]
        data = str(data).replace("u\'",'\'').replace("'",'"')
        print(data)

    if command == "CLOUD":
        devmac = params['devmac']
        sql = "select time, cloudiness from weather where devmac = '%s' order by time desc limit 12" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = []
        cloudy, time = [], []
        for row in rows:
            cloudy.append(eval(row['cloudiness']))
            time.append(str(row['time']))
        newrows = [time, cloudy]
        rows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print(rows)

    if command == "WIND":
        devmac = params['devmac']
        sql = "select time, wind_speed, wind_deg from weather where devmac = '%s' order by time desc limit 12" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = []
        time, speed, deg = [], [], []
        for row in rows:
            time.append(str(row['time']))
            speed.append(eval(row['wind_speed']))
            deg.append(eval(row['wind_deg']))
        newrows = [time, speed, deg]
        rows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print(rows)

    if command == "SDBAY":
        sql = "select groupID, dev_lat, dev_long from devices"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            row['dev_lat'] = str(row['dev_lat'])
            row['dev_long'] = str(row['dev_long'])
        rows = str(rows).replace("u\'",'\'').replace("'",'"')
        print('{"devices" : %s}' % rows)


    if command == "MCDATA":
        devmac = params['devmac']
        sql = "select wind, hum, w.hour from (select avg(wind_speed) wind, substring(time, 12, 2) as hour from weather where devmac='%s' group by hour order by hour) w INNER JOIN (select avg(hum) hum, substring(timerstamp, 12, 2) as hour from mcdata where mac='%s' group by hour order by hour) h ON w.hour = h.hour " % (devmac, devmac)
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = []
        hour, hum, wind = [], [], []
        for row in rows:
            wind.append(row['wind'])
            hum.append(int(row['hum']))
            hour.append(int(row['hour']))
        newrows = [hour, hum, wind]
        newrows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print(newrows)

    if command == "LOGMC":
        gid = "01"
        mac = params['devmac']
        temp = params['temp']
        hum = params['hum']
        time = datetime.now()
        sql = "INSERT INTO mcdata(gid, mac, temp, hum, timerstamp, status) VALUES ('%s','%s', '%s', '%s', NOW(), 'ACTIVE')" % (gid, mac, temp, hum)
        try:
            cursor.execute(sql)
            status = 'OK'
        except:
            status = 'DB Error'
        print("{'timestamp': %s, 'status': %s}" % (time, status))

    if command == "WEATHER":
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'zip': "92130,us", 'appid': "0354c29c5e773c46d37727c8a0455d58"}
        r = requests.get(url, params=params)
        data = r.json()
        #data = str(data).replace("u\'",'\'').replace("'",'"')

        gid = "01"
        timestamp = datetime.now()
        provider = 'Open Weather'
        hum = data['main']['humidity']
        temp = data['main']['temp']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']

        sql = "INSERT INTO forecast(gid, temp, min_temp, max_temp, hum, timestamp, provider) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (gid, temp, min_temp, max_temp, hum, timestamp, provider)
        cursor.execute(sql)

    if command == "PIE":
        devmac = params['devmac']
        sql = "SELECT blemac, count(blemac) as counts FROM iotdb.blelogs where devmac = '%s' group by blemac order by counts desc limit 10" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = [["Device", "Counts"]]
        for row in rows:
            newrows.append([str(row['blemac']), row['counts']])
        newrows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print('{"pie" : %s}' % newrows)


    if command == "HOURLY":
        devmac = params['devmac']
        sql = "select avg(blerssi) as avg_rssi, substring(timestamp, 12, 2) as hour from iotdb.blelogs where devmac='%s' group by hour" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows = []
        for row in rows:
            newrows.append([int(row['hour']), row['avg_rssi']])
        newrows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print('{"hourly" : %s}' % newrows)

    if command == "VISITORS":
        devmac = params['devmac']
        sql = "select count(distinct blemac) as counts, left(timestamp, 10) as date from blelogs where devmac='%s' group by date" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        newrows= []
        for row in rows:
            #row['date'] = str(row['date'])
            newrows.append([row['date'], row['counts'], 'gold'])
        newrows = str(newrows).replace("u\'",'\'').replace("'",'"')
        print('{"visitors" : %s}' % newrows)
    
    if command == 'LIST':
        sql = "SELECT dev_lat, dev_long, mac FROM devices"
        cursor.execute(sql)
        rows = cursor.fetchall()
        rows = str(rows).replace("u\'",'\'').replace("'",'"')
        print('{"devices" : %s}' % rows)

    if command == "LOCATIONS":
        gid = params['gid']
        if gid == "01":
            sql = "SELECT distinct mac, dev_lat, dev_long, groupID, lastseen FROM devices WHERE dev_lat IS NOT NULL AND dev_long IS NOT NULL AND groupID = '%s' " % gid
        else:
            sql = "SELECT distinct mac, dev_lat, dev_long, groupID, lastseen FROM devices WHERE dev_lat IS NOT NULL AND dev_long IS NOT NULL"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            row['dev_lat'] = str(row['dev_lat'])
            row['dev_long'] = str(row['dev_long'])
            row['lastseen'] = str(row['lastseen'])
        rows = str(rows).replace("u\'",'\'').replace("'",'"')
        print('{"devices" : %s}' % rows)

    if command == 'BLELOGS':
        devmac = params['devmac']
        
        sql = "SELECT * FROM blelogs WHERE devmac = '%s' ORDER BY timestamp DESC LIMIT 5" % devmac
        cursor.execute(sql)
        rows = cursor.fetchall()
        time = datetime.now()
        for row in rows:
            lastseen = (time - row['timestamp']).total_seconds()
            if lastseen <= 10:
                row['status'] = 'Last 10 Seconds'
                row['color'] = 'green'
            if lastseen > 10 and lastseen <= 600:
                row['status'] = 'Last 10 Minutes'
                row['color'] = 'yellow'
            if lastseen > 600:
                row['status'] = 'More than 10 Minutes'
                row['color'] = 'red'
            row['timestamp'] = str(row['timestamp'])
            
        rows = str(rows).replace("u\'", "\'").replace("'",'"')

        print('{"blelogs" : %s}' % rows)

    if command == 'GROUPS':
        sql = 'SELECT * FROM groups'
        cursor.execute(sql)
        rows = cursor.fetchall()
        rows = str(rows).replace("u\'", "\'").replace("'",'"')
        print('{"groups" : %s}' % rows)

    if command == 'LOGDEV':
        mac = params['mac']
        gid = params['gid']
        rssi = params['rssi']
        time = datetime.now()
        sql = "INSERT INTO devlogs(mac, groupID, RSSI, lastseen) VALUES ('%s', '%s', '%s', '%s')" % (mac, gid, rssi, time)
        try:
            cursor.execute(sql)
            status = 'OK'
        except:
            status = 'DB Error'
        print("{'timestamp': %s, 'status': %s}" % (time, status))

    if command == 'LOG':
        beacons = ast.literal_eval(params['beacons'])
        mac = params['devmac']
        gid = params['gid']
        time = datetime.now()
        sql = "INSERT INTO blelogs(gid, devmac, blemac, blerssi, timestamp) VALUES " 

        for idx, beacon in enumerate(beacons):
            blemac = beacon['mac']
            blerssi = beacon['rssi']
            row = "('%s', '%s', '%s', '%s', '%s')" % (gid, mac, blemac, blerssi, time)
            if idx < len(beacons)-1:
                sql += row + ','
            else:
                sql += row + ';'
        try:
            cursor.execute(sql)
            connection.commit()
            status = 'Stored'
        except:
            status = 'DB Error'
        print("{'timestamp': %s, 'status': %s}" % (time, status))

        #updating timestamp in devices table
        sql_update = "UPDATE devices SET lastseen='%s' WHERE mac='%s'" % (time, mac)
        try:
            cursor.execute(sql_update)
            status = 'Updated'
        except:
            status = 'DB Error'
        print("{'timestamp': %s, 'status': %s}" % (time, status))



    if command == 'REG':
        mac = params['mac']
        gid = params['gid']
        ip = params['ip']
        time = datetime.now()

        #sql query to check if mac address is already in devices
        sql_exists = "SELECT * FROM devices WHERE mac='%s'" % mac
        cursor.execute(sql_exists)
        search_result = cursor.fetchall()

        #if length of search results greater than 0, update the existing record
        if len(search_result) > 0:
            sql = "UPDATE devices SET lastseen='%s' WHERE mac='%s'" % (time, mac)
            try:
                cursor.execute(sql)
                status = 'OK'
            except:
                status = 'DB Error'
            print("{'timestamp': %s, 'mac', %s, 'status': %s}" % (time, mac, status))
        else:
            if mac != "":
                sql = "INSERT INTO devices(groupID, mac, lastseen, ip) \
                    VALUES ('%s', '%s', '%s', '%s')" % (
                        gid, 
                        mac,
                        time,
                        ip
                    )
                try:
                    cursor.execute(sql)
                    status = 'OK'
                except Exception as E:
                    print(E)
                    status = 'DB Error'
                print("{'timestamp': %s, 'mac', %s, 'status': %s}" % (time, mac, status))

connection.close()
