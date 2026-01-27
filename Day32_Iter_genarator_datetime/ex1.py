import datetime

td=datetime.datetime.now()
print(td)
dt1=datetime.datetime(day=31,year=2025,month=12,hour=10,minute=10,second=10)
print(dt1)
dt2=datetime.datetime(2025,12,1,10,10,10)
print(dt2)
print(dt1-dt2)

dt3=datetime.datetime.strptime('2026-1-12','%Y-%m-%d')
print(type(dt3))

dt4=datetime.datetime.now()
print(dt4.strftime('%Y-%m-%d %H:%M:%S'))

dt5=dt4-datetime.timedelta(minutes=100)
print(dt5)