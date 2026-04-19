# DATE AND TIMES USING PYTHON

import datetime

date = datetime.date(2026, 1, 27)
print(date)  # OUT -> 2026-01-27

today = datetime.date.today()
print(today)  # OUT -> 2026-04-19

time = datetime.time(12, 30, 0)
print(time)  # OUT -> 12:30:00

now = datetime.datetime.now()
print(now)  # OUT -> 2026-04-19 14:47:57.141721

now2 = now.strftime("%H %M %S")
print(now2)  # OUT -> 14 49 00

now3 = now.strftime("%H:%M:%S")
print(now3)  # OUT -> 14:49:00

now4 = now.strftime("%H:%M:%S %d-%m-%Y")
print(now4)  # OUT -> 14:52:27 19-04-2026

target_datetime = datetime.datetime(2039, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed") # This
