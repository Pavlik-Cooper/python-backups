cities = ["New York", "Tokyo", "London", "Toronto", "Kiev"]

with open('cities.txt', 'w') as cities_file:
    for city in cities:
        cities_file.write(city)

with open('cities.txt', 'w') as cities_file:
    for city in cities:
        print(city, file=cities_file, end=";\n")


cities_from_file = []
with open('cities.txt','r') as cities:
    for city in cities:
        cities_from_file.append(city.strip(';\n'))

print(cities_from_file)


imelda = "More Mayhem", "Imelda Bla", 1988, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Whatsoever"))


with open('tuple_file.txt','w') as tuple_file:
    print(imelda, file=tuple_file)


with open('tuple_file.txt') as tuple_file:
    contens = tuple_file.readline()
    contens = eval(contens)

print(contens)
