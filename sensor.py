#!/usr/bin/python3
# -*- Coding: UTF-8 -*-

import os
import time
import Adafruit_DHT

# Sensor information
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Create new file or resume old one
path = os.path.dirname(os.path.abspath(__file__))
filename = '{0}/data.csv'.format(path)
try:
    f = open(filename, 'a+')
    if os.stat(filename).st_size == 0:
            f.write('timestamp,temperature,humidity\r\n')
except:
    pass

# Get data and save into file
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        row = '{0},{1:0.1f},{2:0.1f}\r\n'.\
        format(time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity)
        #print(row)
        f.write(row)
        f.flush()
    else:
        print("Failed to retrieve data from sensor")
    # Define interval measures (in seconds)
    time.sleep(60)
