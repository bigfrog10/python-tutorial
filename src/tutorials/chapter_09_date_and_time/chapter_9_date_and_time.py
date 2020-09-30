# we postpone the date/time data type to now because it's more complicated than
# it looks like.
# First there are many packages/libs
#     Python standard libs: datetime, time, calendar
#     dateutil, 3rd party lib mentioned in pydoc
#     pytz
#     arrow
#     pendulum
#     maya
#     dateparser
#     numpy version
#     cftime
#     moment

# we deal with time, date, date time, calendar, and duration
# These interact with timezone, daylight saving time, and holidays.

import time  # This is required to include time module.
import calendar
import datetime

# time start point/epoch = 12:00am, January 1, 1970 UTC (Greenwich)
# https://en.wikipedia.org/wiki/Coordinated_Universal_Time
# most systems use this epoch, but others show up too. So check first.
# return datetime objects
# timezone, including daylight impact, has only local and utc in
# datetime. So use local timezone internally and use utc externally.
# Need to deal with database separately.
EPOCH = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
print('system epoch: ', EPOCH)
# Not used by system, but show the timezone diff. No daylight saving.
print(f'epoch in local time: {datetime.datetime.fromtimestamp(0)}')

local_delta = datetime.datetime.utcfromtimestamp(0) - datetime.datetime.fromtimestamp(0)
local_tz = datetime.timezone(local_delta)
print(datetime.datetime(2020, 9, 30, tzinfo=local_tz))  # 2020-09-30 00:00:00+05:00
# above doesn't count daylight saving time.

# time resolution
# 1 second = 1,000 millisecond, ms
#          = 1,000,000 microseconds, µs
#          = 1,000,000,000 nanoseconds, ns
# Ideally, we should go with ns, which is the hardware resolution.
# Other libs, like numpy, use ns.
print(f'time resolution: {datetime.time.resolution}')  # 1 µs, return timedelta

# daylight saving is factored in. It's 4 hrs diff, but epoch diff is 5 hrs.
print(f'local now: {datetime.datetime.now()}')  # datetime object
print(f'utc now: {datetime.datetime.utcnow()}')  # datetime object
print(f'local today: {datetime.datetime.today()}')  # almost same as now()

# this is None. Native/aware
print(f'local timezone: {datetime.datetime.now().tzinfo}')

# use this to figure out the timezone with daylight saving
local_delta = datetime.datetime.utcnow() - datetime.datetime.now()
local_tz = datetime.timezone(local_delta)
print(datetime.datetime(2020, 9, 30, tzinfo=local_tz))  # 2020-09-30 00:00:00+04:00

# formatting and parsing
print(f'local now str: {datetime.datetime.now().strftime("%Y-%m-%d")}')
print(f'local now str: {datetime.datetime.now().strftime("%Y%m%d")}')
print(f'parse string: {datetime.datetime.strptime("04/26/2020", "%m/%d/%Y")}')

# delta
d1 = datetime.datetime(2020, 9, 30, 1, 6, 35)
d2 = datetime.datetime(2020, 11, 3, 0, 0, 0)
duration = d2 - d1  # timedelta class, operator overload
print(f'{duration} days left for election')
print(f'{duration.total_seconds()} seconds left for election')
# convert total seconds to other units, minutes, hours, etc.

# not working for months and above
duration = datetime.timedelta(weeks=1)
print(f'a week later: {d1} to {d1 + duration}')  # operator overload

# if we need months and years, start from a datetime and change months and
# years.
print(d1.replace(year=d1.year+1))  # this does not work for leap years
# another way is dateutil.relativedelta.

# date class
print(datetime.date.today())  # return date object
print(datetime.date(2020, 4, 26))
d = datetime.date(2020, 4, 26)
print(datetime.datetime(d.year, d.month, d.day))  # convert to datetime

# There is also datetime.time for time only.

# There is another module, time, which has some different features.
# interesting but not widely used.
print(time.timezone)  # 5 hrs, no daylight
print('epoch=', time.gmtime(0))  # time.struct_time(tm_year=1970, ...
print('now=', time.gmtime())  # time.struct_time(tm_year=2020, ...

print("now in seconds since epoch:", time.time())  # as float
print("now in nanoseconds since epoch:", time.time_ns())  # as int
print("now in English: ", time.ctime(time.time()))  # as str

print(time.localtime())  # as struct_time for separate fields in time.
print(time.localtime(time.time()))

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

time.sleep(1)  # I guess this is the most widely used function, seconds.
# when timezone is needed, check Python 3.9 new feature, or dateutil,
# or pytz.

# Python's calendar, this class is mainly for display purpose, text or html
print(calendar.isleap(2017))  # False
print(calendar.isleap(2020))  # True
print(calendar.weekday(2020, 11, 3))  # 1 means Tuesday, 0 is Monday

cal = calendar.month(2020, 4)
print(cal)  # this class is mainly for display purpose, text or html

# +/- calendar days, week days, months (need to adjust end days)

# Business calendars can be modeled as a chronicle calendar with a list of
# holidays. The holidays depend on many factors, could be a national holiday,
# a local city holiday, etc. Need to be able to customize.

# pandas has a class AbstractHolidayCalendar that can be extended. This seems
# the right way to model this.
# https://analyzingalpha.com/time-series-analysis-with-python
# https://www.dataquest.io/blog/python-datetime-tutorial/
