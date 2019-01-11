# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Sam Print only the words that start with s in this sentence'

st_splitted = st.split()

# 1)
s_words = [w for w in st_splitted if w.lower().startswith("s")]

print(s_words)

# 2)

# s_words = []
# for w in st_splitted:
#     if w[0] == "s":
#         s_words.append(w)

# print(s_words)


# 2. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

nums = [num for num in range(1,51) if num % 3 == 0]
print(nums)


# 3. Go through the string below and if the length of a word is even print "even!"

# st = 'Print every word in this sentence that has an even number of letters'
#
# st_splitted = st.split()
#
# even_words = [f"{w} is even" for w in st_splitted if len(w) % 2 == 0]
# print(even_words)
#
# for w in st_splitted:
#     if len(w) % 2 == 0:
#         print(f"{w} is even")
#
# print(even_words)



# 4   Write a program that prints the integers from 1 to 100.
    # But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
    # For numbers which are multiples of both three and five print "FizzBuzz".
#
# for n in range(1,25):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz", n)
#         # print(n)
#     elif n % 3 == 0:
#         print("Fizz",n)
#         # print(n)
#     elif n % 5 == 0:
#         print("Buzz",n)
#         # print(n)
#     else:
#         print(n)

# 5 Use List Comprehension to create a list of the first letters of every word in the string below:

# st = 'Create a list of the first letters of every word in this string'
#
# st_splitted = st.split()
#
# fst_letters = [w[0] for w in st_splitted]
#
# print(fst_letters)

print(help(list().insert))
