import pdb

x = [1,2,3]
y = 5
z = 6
a = y + z
print(a)


pdb.set_trace()

b = x + y   # bug
print(b)