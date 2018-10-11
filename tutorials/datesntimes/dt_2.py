import datetime

# working with hours, minutes, secs, and micro-seconds
t = datetime.time(9, 30, 45, 100000)
print(t)

print(t.hour)   # accessing components

# datetime.date ==> just date
# .time ==> just time
# .datetime ==> date + time

t = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(t)

# grabbing just the date
print(t.date())


# grabbing just the time
print(t.time())


# grabbing just the year, etc.
print(t.year)


# aritmetic with timedeltas still works
tdelta = datetime.timedelta(hours=12)
print(t + tdelta)



