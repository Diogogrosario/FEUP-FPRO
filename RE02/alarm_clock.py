import datetime
now=datetime.datetime.now()
print(now.strftime("%H:%M"))

delta= datetime.timedelta(hours=8,minutes=30)

d2=now+delta

print(d2.strftime("%H:%M"))



