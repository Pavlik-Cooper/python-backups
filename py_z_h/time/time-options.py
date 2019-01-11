# Щоб вичислити скільки пройшло часу, використовуй  perf_counter

import time
from time import perf_counter as timer  # time.time, perf_counter, monotonic
from random import randint

input("Press enter to start ")

wait_time = randint(1,3)
time.sleep(wait_time)
start_time = timer()

input("Press enter to stop ")
end_time = timer()

print("Started at {}".format(time.strftime("%X",time.localtime(start_time))))
print("Ended at {}".format(time.strftime("%X",time.localtime(end_time))))

# print(end_time - start_time)
print("Yor reaction time was {} seconds".format(time.strftime("%-S",time.localtime(end_time - start_time))))



print("==========================")

print("time()\t\t", time.get_clock_info('time'))
print("perf_counter()\t", time.get_clock_info('perf_counter'))
print("monotonic()\t", time.get_clock_info('monotonic'))
print("process_time()\t", time.get_clock_info('process_time'))
