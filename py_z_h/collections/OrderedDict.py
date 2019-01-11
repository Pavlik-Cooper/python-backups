from collections import OrderedDict

d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3

d2 = {}
d2['b'] = 2
d2['a'] = 1
d2['c'] = 3

print(d1 == d2)  # true -- no matter in what order

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
d2['c'] = 3

print(d1 == d2)  # false -- order matters