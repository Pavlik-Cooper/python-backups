from collections import namedtuple

Dog = namedtuple('dog', 'name age fur')

sam = Dog('sam', 5, 'fuzzy')

print(sam[0])
print(sam.age)  # cannot access like this sam['age']

