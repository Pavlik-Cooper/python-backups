fruit = {"apple":"nice fruit", "pear":"also","orange":"citrus","banana":"yellow", "grape": "sweet"}


# print(fruit.get("avocado"))  # won't raise a KeyError
# print(fruit.get("avocado", "We don't have such fruit"))  # default val


# while True:
#     dict_key = input("Enter a fruit ")
#     if dict_key == "":
#         continue
#     if dict_key in ["quit", "exit"]:
#         break
#     print(fruit.get(dict_key, f"We don't have {dict_key}"))

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

print("="*25)

keys = fruit.keys()
fruit["pineapple"] = "pineapple"

print(keys)


f_tuple = tuple(fruit.items())
print(f_tuple)

f_dict = dict(f_tuple)
print(f_dict)

t_dict = dict((("haha", "bad"), ("another", "val")))
print(t_dict)


dict_with_tuple_key = {('foo','bar'):"foobar", (1,2): (1,2),('foo','baz'):"foobar"}

print(dict_with_tuple_key)

# del fruit["pear"]
# fruit.clear()
# print(fruit)
