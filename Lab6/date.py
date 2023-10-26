# 1.Write a Python program to subtract five days from current date.
import datetime
dt = datetime.date.today()
nd = dt-datetime.timedelta(days=5)
print(dt) #today
print(nd) #5 days from current date

# 2.Write a Python program to print yesterday, today, tomorrow.
import datetime
dt = datetime.date.today()
yd = dt-datetime.timedelta(days=1)
tw = dt+datetime.timedelta(days=1)
print(dt) #today
print(yd) 
print(tw)

# 3.Write a Python program to drop microseconds from datetime.
import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)

# 4.Write a Python program to calculate two date difference in seconds.
from datetime import date
x = date(2023, 10, 19)
y = date(2023, 9, 1)
dif = (x-y).total_seconds()
print(dif)
