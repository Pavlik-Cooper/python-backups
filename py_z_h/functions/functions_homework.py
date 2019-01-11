import string

""" Write a function that computes the volume of a sphere given its radius. """

def vol(rad):
    pass

""" Write a function that checks whether a number is in a given range (inclusive of high and low) """

def ran_bool(num,low,high):
   # 1)
     return num >= low and num <= high
  # 2) return num in range(low,high+1)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
    uppers = 0
    lowers = 0
    for l in s:
        if l.isupper():
            uppers += 1
        elif l.islower():
            lowers += 1
    return f"No. of Upper case characters : {uppers} \nNo. of Lower case Characters : {lowers}"

# print(up_low(s))


""" Write a Python function that takes a list and returns a new list with unique elements of the first list."""

def unique_list(lst):
    unique = []
    [unique.append(n) for n in lst if n not in unique]
    return unique


# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


""" Write a Python function to multiply all the numbers in a list. """

def multiply(numbers):
    num = numbers.pop(0)
    for n in numbers:
        num *= n
    return num


# print(multiply([1,2,3,-4]))

""" Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""

s = "nursesrun"

def palindrome(st):
    st = "".join(st).lower()
    return st[::-1] == st


# print(palindrome(s))


""" Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog """


def ispangram(str1, alphabet=string.ascii_lowercase):
    # 1)
    # alphabet = list(alphabet)
    # str1 = str1.lower()
    # for l in str1:
    #     if l in alphabet:
    #         alphabet.remove(l)
    #
    # return len(alphabet) == 0

    # 2)
    alphaset = set(alphabet)
    return  set(str1.lower()) >= alphaset  # set(["a","b","c"]) >= set(["a","b","c"])


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("J.Q. Schwartz flung V.D. Pike my box"))



