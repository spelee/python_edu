import datetime
import pytz         # recommended module for timezones

# alternative constructors

# none of the ways below give tz 'aware' datetimes

dt_today = datetime.datetime.today() # current local datetime, tz is None

# gives option to pass a timezone, so not passing a tz makes it equivalent to today()
dt_now = datetime.datetime.now()

# gives utc time, but actually *not* tz aware (i.e. empty tzinfo)
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


# recommendation is to work with utc timezone
# left of micro seconds in this example
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)  # the +00:00 is the tz offset


print(datetime.datetime.now())

# current utc time that is also timezone aware
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)


# an alternative way to get current utc time that is also tz aware
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# now in a different timezone
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print(dt_mtn)

print('\n', '='*80, '\n')

# all timezones
for tz in pytz.all_timezones:
    break
    print(tz)

print('\n', '='*80, '\n')

# localize() converts naive time to local time (i.e. tz aware)
# this method should be used to construct localtimes, rather than passing tzinfo argument to a datetime constructor
dt_mtn = datetime.datetime.now()
print("Naive local time:")
print(dt_mtn)
print()

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print("Converted to tz aware time for different tz:")
print(dt_east)
print()

print("Original local time is still naive:")
print(dt_mtn)
print()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print("Now, local time is tz aware.  But note, did not localize to my actual tz.")
print("Localized to Mountain time instead of Pacific.")
print(dt_mtn)
print()

# The following statement no longer seems to be true...
# Can only convert tz if it is a timezone aware (i.e. localized tz)

# And now converting the tz again...
print("Converting tz aware local to new tz, Eastern again.  Except now from Mountain time.")
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
print()

# iso format
print("Printing in ISO format")
print(dt_mtn.isoformat())
print()

# my own format.  example...
print("Personalized formatting for datetime")
print(dt_mtn.strftime('%B %d, %Y'))
print()

# parsing date string into datetime obj
print("Parsing string into datetime")
dt_str = 'October 10, 2018'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
print()

