import time

print(time.time())  # number representation

print(time.gmtime())   # current GMT time
print(time.localtime())  # local time

print(time.gmtime(0))  # 1 Jan 1970
print(time.localtime(0))  # 1 Jan 1970

print("=================")

loc_time = time.localtime()

print("Year - ", loc_time.tm_year)
print("Day - ", loc_time.tm_mday)
print("Hour - ", loc_time.tm_hour)

print(time.localtime(time.time() + 3600))  # current time plus 1 hour



