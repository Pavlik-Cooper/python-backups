string = "quick brown"


print("\n list from string")

list_from_str = [l for l in string]
print(list_from_str)


print("\n a regular list")

my_list = [num for num in range(0,11)]
print(my_list)


print("\n list with squared numbers")

my_list = [num ** 2 for num in range(0,11)]   #  same as [num * num for num in range(0,11)]
print(my_list)



print("\n celcious to farenheit conversion \n")

celcious = [0,10,20,34.5]

farenheit = [ ((9/5) * deg + 32) for deg in celcious]

print(farenheit)


print("\n list comp with if statement \n")

my_list = [num * num for num in range(0,11) if num % 2 == 0]

print(my_list)


print("\n list comp with if else statement \n")

my_list = [num if num % 2 == 0 else 'Odd' for num in range(0,11)]

print(my_list)


print("\n list comp like nested loop \n")

my_list = [a * b for a in [2, 4, 6] for b in [100, 200, 600]]

print(my_list)

lst = [["foo","bar"], ["foo","baz"]]




