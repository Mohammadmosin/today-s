import datetime
a = datetime.datetime(2017, 6, 21, 18, 25, 30)
b = datetime.datetime(2017, 5, 16, 8, 21, 10)
c = a - b
print('Difference: ', c)
minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)
# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)
a = datetime.datetime(2017, 6, 21, 18, 25, 30)
b = datetime.datetime(2017, 5, 16, 8, 21, 10)
print(type(b))
# returns a timedelta object
c = a - b
print('Difference: ', c)
print(type(c))
# returns (minutes, seconds)
minutes = divmod(c.total_seconds(), 60)
print('Total difference in minutes: ', minutes[0], 'minutes',
      minutes[1], 'seconds')

# returns the difference of the time of the day (minutes, seconds)
minutes = divmod(c.seconds, 60)
print('Total difference in minutes: ', minutes[0], 'minutes',
      minutes[1], 'seconds')