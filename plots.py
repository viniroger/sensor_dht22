#!/usr/bin/python3
# -*- Coding: UTF-8 -*-

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get dataframe from CSV file
filename = 'data.csv'
df = pd.read_csv(filename)

# Convert into datetime format
x_orig = df.timestamp
df.timestamp = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x_orig]

# Figure info
fig = plt.figure()
fig, ax1 = plt.subplots()
fig.autofmt_xdate()

ax1.set_ylabel('Temperatura (°C)', color='r')
ax1.tick_params('y', colors='r')
lns1 = plt.plot(df.timestamp,df.temperature, marker='.', linestyle='-', color='r')

plt.suptitle('Temperatura e Umidade - DHT22', fontsize=12)
plt.minorticks_on()
plt.grid(which='major', linestyle='--')
plt.grid(which='minor', linestyle=':')

ax2 = ax1.twinx()
lns2 = ax2.plot(df.timestamp,df.humidity, marker='.', linestyle='-', color='b')
ax2.set_ylabel('Umidade (%)', color='b')
ax2.tick_params('y', colors='b')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))

# Save figure
figname = 'plot_ts.png'
plt.savefig(figname)
