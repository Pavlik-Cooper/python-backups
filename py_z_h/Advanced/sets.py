s = {1, 2, 3}
s.add(4)

a = s.copy()
s.add(8)

set1 = {1, 2, 3, 4}
set2 = {1, 4, 5}

# print(set1.difference(set2))
# set1.difference_update(set2)

# print(set1.intersection(set2))
# set1.intersection_update(set2)

set1 = {1, 2, 3, 4}
set2 = {5}

# print(set1.isdisjoint(set2))  # returns True if there's no intersection at all

# print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)

# set1.update(set2)  # merges two lists

united_set = set1.union(set2)

# print(united_set)

set1 = {1, 2, 3, 4}
set2 = {1, 2}

# print(set1.issuperset(set2))
# print(set2.issubset(set1))

set1.remove(2)  # removes item if it exists, otherwise throws KeyError
set1.discard(9)  # removes item if it exists but if it doesn't then no error wil be thrown
print(set1)

set1.clear()

print(set1)