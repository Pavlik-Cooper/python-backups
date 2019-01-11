print(range(0,5,2) == range(0,6,2))
print(list(range(0,5,2)) == list(range(0,6,2)))

print(range(0, 100)[::-2] == range(99, 0, -2))

r = range(45)
print(list(r[::-1]))  # (negative step) 44 -- 0
print(list(r[::-2]))  # 44 - 1
print(list(r[20:3:-2]))  # (start == 20: stop == 3: step -2)   20 - 4

print("="*40)

for n in r[::-2]:
    print(n)

print("="*40)

for n in r[:30:-2]:  # only stop and step
    print(n)

print("="*40)

for n in r[40:30:-2]:
    print(n)


print("="*40)

o = range(0,100,4)

print(o)
print(list(o))

p = o[::5]  # step now is being multiplied
print(p)
print(list(p))  # step now is multiplied -- 20
