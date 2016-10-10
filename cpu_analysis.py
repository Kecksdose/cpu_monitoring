#!/Users/tschmelzer/anaconda3/bin/python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import datetime

# Read data
logfile = '/Users/tschmelzer/cpu_monitoring/cpu.log'

df = pd.read_csv(logfile, sep=';')

# Convert timestamps in arrow format
df.timestamp = [datetime.datetime.strptime(cur_time, '%d.%m.%Y,%H:%M:%S')
                for cur_time in df.timestamp]

# Filter unusual values after awaking the system
df = df[df.cpu_temperature != 127.0]

# Configure plot
plt.figure(figsize=(12, 8))
glob_fontsize = 16

# Set date format to x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m %H:%M:%S'))

# Plot temperature
plt.plot(df.timestamp, df.cpu_temperature, 'b')
plt.gca().set_ylabel('Temperatur (C°)', color='b', fontsize=glob_fontsize)
for tl in plt.gca().get_yticklabels():
    tl.set_color('b')
    tl.set_fontsize(glob_fontsize - 2)

# Plot fan speed
plt.gca().twinx()
plt.plot(df.timestamp, df.fan_speed, 'g')
plt.gca().set_ylabel('Fan speed (RPM)', color='g', fontsize=glob_fontsize)
for tr in plt.gca().get_yticklabels():
    tr.set_color('g')
    tr.set_fontsize(glob_fontsize - 2)

# Format date angle
plt.gcf().autofmt_xdate()

# Other configurations
plt.title('CPU Temperatur und Kühlergeschwindigkeit', fontsize=glob_fontsize+2)
plt.savefig('/Users/tschmelzer/cpu_monitoring/cpu_cpu_and_fanspeed.pdf')



