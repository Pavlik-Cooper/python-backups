from collections import defaultdict


d = defaultdict(object)  # set an empty object by def

print(d['key2'])  # // <object object at 0x7f50288690a0>

for item, val in d.items():
    print(item, val)

d = defaultdict(lambda : 0)

print(d["sddd"])  # 0