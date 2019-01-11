list1 = [1,2,3]

another_list = list1
print(another_list == list1)  # True

another_list = sorted(list1)
print(another_list == list1)  # True

list1 = [3,2,1]
another_list = sorted(list1, reverse=True)
print(another_list == list1)  # True

list1 = [3,2,1]
another_list = sorted(list1)
print(another_list == list1)  # False

another_list = list1.copy()
print(another_list is list1)  # False

another_list = sorted(list1, reverse=True)
print(another_list is list1)  # False

another_list = list1
print(another_list is list1)  # True

print("list unpacking")

my_list = [1, 2, 3]
a, b, c = my_list

print(b)

