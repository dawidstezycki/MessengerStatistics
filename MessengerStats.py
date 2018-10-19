#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import json
from datetime import datetime, timedelta
import matplotlib.dates as mdates

with open("message.json", "r") as read_file:
    data = json.load(read_file)

you = u'Dawid Stężycki'
partner = "Partner"

for message in data['messages']:
	message['sender_name'] = message['sender_name'].encode('raw_unicode_escape').decode('utf-8')
	if 'content' in message:
		message['content'] = message['content'].encode('raw_unicode_escape').decode('utf-8')

startTimeStamp = int(data['messages'][-1]['timestamp_ms']/1000)
start_time = datetime.fromtimestamp(startTimeStamp)
print start_time

endTimeStamp = int(data['messages'][0]['timestamp_ms']/1000)
end_time = datetime.fromtimestamp(endTimeStamp)
print end_time

nbr_days = (end_time - start_time).days
print("Number of days: " + str(nbr_days))

nbr_msg = len(data['messages'])
print("Number of messages: " + str(nbr_msg))

nbr_words = 0
for message in data['messages']:
	if 'content' in message:
		nbr_words += len(message['content'].split())
print("Number of words: " + str(nbr_words))

avg_len_msg = round(nbr_words / nbr_msg, 1)
print("Average length of messages: " + str(avg_len_msg) + " words")

avg_msg_per_day = round(nbr_msg / nbr_days, 1)
print("Average messages per day: " + str(avg_msg_per_day))


# Plot of who texts the most
nbr_you = 0
nbr_partner = 0
for message in data['messages']:
	if message['sender_name'] == you:
		nbr_you += 1
	else:
		nbr_partner += 1

procentage_you = 100 * round(nbr_you / float(nbr_msg), 2)
procentage_partner = 100 * round(nbr_partner / float(nbr_msg), 2)
fracs = [procentage_you, procentage_partner];
labels = [you, partner]
colors = ['#8c000f', '#F08080']
pie = plt.pie(fracs, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
plt.axis('equal')
plt.title("Who texts the most?")
plt.show()
print("Number of times " + you + ": " + str(nbr_you) + ' (' + str(procentage_you) + '%)')
print("Number of times " + partner + ": " + str(nbr_partner) + ' (' + str(procentage_partner) + '%)')

# Fetch timeline data
timeline = [None] * (nbr_days + 2)
hour = list(range(24))
weekday_arr = [0, 1, 2, 3, 4, 5, 6]
nbr_times_hour = [0] * 24
nbr_times_weekday = [0] * 7
nbr_times_day = [0] * (nbr_days + 2)
current_day = end_time.date()
index = len(timeline) - 1
timeline[index] = current_day
nbr_times_day[index] = 1
for message in data['messages']:
    currentStamp = int(message['timestamp_ms']/1000)
    current = datetime.fromtimestamp(currentStamp)
    h = current.hour + current.minute / 60. + current.second / 3600
    h = int(round(h))
    if h == 24:
        h = 0
    nbr_times_hour[h] = nbr_times_hour[h] + 1
    wd = current.weekday()
    nbr_times_weekday[wd] = nbr_times_weekday[wd] + 1
    current = current.date()
    if current == current_day:
        nbr_times_day[index] = nbr_times_day[index] + 1
    elif current < current_day:
        diff = (current_day - current).days
        index = index - diff
        current_day = current
        timeline[index] = current_day
        nbr_times_day[index] = 1
dates = [None] * len(timeline)
for i in range(0, len(timeline)):
    if timeline[i] == None:
        timeline[i] = timeline[i - 1] + timedelta(days=1)
    dates[i] = timeline[i].strftime("%Y-%m-%d")

# Plot timeline
fmt = mdates.DateFormatter('%Y-%m-%d')
ax = plt.axes()
ax.xaxis.set_major_formatter(fmt)
plt.bar(timeline, nbr_times_day, align="center", color='#8c000f',edgecolor = '#8c000f')
plt.title("Timeline")
ax = plt.axes()
ax.yaxis.grid(linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
fig = plt.figure(1)
fig.autofmt_xdate()
plt.show()

# Plot by hour
plt.bar(hour, nbr_times_hour, align="center", width=0.8, color='#8c000f')
plt.title("Activity by Day")
plt.xlim((-0.8,23.8))
ax = plt.axes()
ax.yaxis.grid(linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
fig = plt.figure(1)
plt.show()

# Plot by weekday
weekday_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.bar(weekday_arr, nbr_times_weekday, align="center", width=0.8, color='#8c000f')
plt.xticks(weekday_arr, weekday_labels)
plt.title("Activity by Week")
ax = plt.axes()
ax.yaxis.grid(linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
fig = plt.figure(1)
plt.show()

# Most messages in one day
most_msg = max(nbr_times_day)
print("Most messages in one day: " + str(most_msg))