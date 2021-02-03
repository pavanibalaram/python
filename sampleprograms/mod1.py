import hello
import time
from datetime import datetime,timedelta
now=datetime.now()
print(now)
then=datetime(2020,12,31)
delta=now-then # computes date difference
print(delta)
t=datetime.today() # used for today date
print("today date:", t)
s=time.time()
print(s)