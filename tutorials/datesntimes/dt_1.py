import datetime



# there are 'aware' and 'naive' datetimes.  'aware' datetimes know their timezone and how to track dst.
# 'naive' datetimes do not.

# creating a datetime
d = datetime.date(2016, 7, 24)

print(d)


# today's local date
tday = datetime.date.today()
print(tday)


# grabbing just the year, day, etc.
print(tday.day)
print(tday.year)


# day of the week
print(tday.weekday())    # Monday=0; Sunday=6
print(tday.isoweekday()) # Monday=1; Sunday=7


# timedeltas
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # date 1 week from now
print(tday - tdelta)  # date 1 week ago


# aritmetic between dates gives us an answer in timedeltas
# days until my birthday
bday = datetime.date(2018, 12, 13)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)  # print just the days
print(till_bday.total_seconds())  # print in seconds
