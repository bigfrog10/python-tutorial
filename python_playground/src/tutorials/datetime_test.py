import time  # This is required to include time module.
import calendar
import datetime

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print(localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

cal = calendar.month(2020, 4)
print(cal)

print(datetime.datetime.today())
print(datetime.date.today())
print(datetime.date(2020, 4, 26))
d = datetime.date(2020, 4, 26)
print(d)
print(d.strftime('%Y-%m-%d'))
print(datetime.datetime.strptime("04/26/2020", "%m/%d/%Y"))
print(d.strftime('%Y%m%d'))

# search "python document"
# interactive mode -> terminal


