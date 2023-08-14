import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1998, month=2, day=4, hour=9, minute=39, second=22)
print(date_of_birth)