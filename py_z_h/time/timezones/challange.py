import datetime
import pytz

# print(pytz.all_timezones)
# exit()
# for x in pytz.all_timezones:
#     print(x)


available_timezones = {
 1: "Africa/Tunis",
 2: "Europe/Kiev",
 3: "Japan",
 4: "Europe/Uzhgorod",
 5: "Europe/Vaduz",
}

print("Choose a timezone: ")
for x in sorted(available_timezones):
    print(x, available_timezones[x])

while True:
    choice = int(input())
    if choice == 0: break

    timezone = pytz.timezone(available_timezones[choice])
    world_time = datetime.datetime.now(tz=timezone)
    print("The time in {} is {} {}".format(timezone, world_time.strftime("%A %x %X %z"), world_time.tzname()))
    print("Local time is {}".format(datetime.datetime.now().strftime("%A %x %X")))
    print("UTC time is {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
    print()







