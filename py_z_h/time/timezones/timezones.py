import time

# DST - Daylight saving time

print("The epoch on this system starts at {}\n".format(time.strftime("%c", time.gmtime(0))))
print("The current  timezone is {} with an offset of {}\n".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Daylight savings are in effect for this location\n")
    print("The DST timezone is {}\n".format(time.tzname[1]))


# Greenwich Mean Time (GMT) is often interchanged or confused with Coordinated Universal Time (UTC).
# But GMT is a time zone and UTC is a time standard.

# GMT is a time zone officially used in some European and African countries.
# The time can be displayed using both the 24-hour format (0 - 24) or the 12-hour format (1 - 12 am/pm).

# UTC is not a time zone, but a time standard that is the basis for civil time and time zones worldwide.
# This means that no country or territory officially uses UTC as a local time.

print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))