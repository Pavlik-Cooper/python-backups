text = set("sdfhaioeu")
vowels = frozenset("aouie")

text = text.difference(vowels)
print(sorted(text))

numset = set(range(0,20,2))
print(numset)

tup = (5,8,5,8,5,9)
tuple_set = set(tup)
print(tuple_set)

dic = {"a":"b","b":"c"}
dict_set = set(dic)
print(dict_set)  # only keys