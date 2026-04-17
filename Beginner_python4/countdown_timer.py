import time

#time.sleep(3)


my_time = int(input("Enter sleep time in secs: "))

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")


# # OUTPUT:
# Enter sleep time in secs: 3604
# 01:00:04
# 01:00:03
# 01:00:02
# 01:00:01
# 01:00:00
# 00:59:59
# 00:59:58
# 00:59:57
# 00:59:56
# 00:59:55
# 00:59:54
# 00:59:53
# 00:59:52
# 00:59:51
# 00:59:50
# 00:59:49
# 00:59:48
# 00:59:47
# 00:59:46
# 00:59:45
# 00:59:44
# 00:59:43
# 00:59:42
