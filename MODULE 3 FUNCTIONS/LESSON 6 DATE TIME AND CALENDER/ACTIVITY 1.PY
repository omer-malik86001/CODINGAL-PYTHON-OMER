from datetime import datetime,date
import calendar
now=datetime.now()
print(now)
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(calendar.month(1987,3))
import time
print(time.time()) # SECONDS ELAPSED SINCE EPOCH JANUARY 1 1970
