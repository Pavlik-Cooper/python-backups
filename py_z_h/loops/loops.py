from random import randint,shuffle

my_nums = [0,1,2,3,4]
big_nums = [100,200,300]
my_dic = {"key1":"val1","key2":"val2"}

# shuffle works in place
shuffle(big_nums)

print(big_nums)

# for a,b in my_dic.items():
#     print(a)

# for num in my_nums:
#     if num % 2 != 0:
#         print(f"odd number: {num}")

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print(f"i is not less than 10")


# print(list(range(10)))

# for i in range(1,10,2):
#      print(i)

# for index, l in enumerate("my_str"):
#      print("letter {} at index {}".format(l,index))

#
# for item in zip(my_nums,["a","b","c","d"],big_nums):
#      print(item)


# print("key1" in my_dic) # True
#
# print("a" in "apple") #True

print(randint(0,8))

#
# result = int(input("Input some number: "))
# print(type(result))

print(int(False)) #  0

print(600 not in big_nums)
print(not 600 in big_nums)
