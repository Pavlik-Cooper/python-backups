# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min([a,b])
#     return max([a,b])
#
# print(lesser_of_two_evens(5,7))
#
# def animal_crackers(text):
#     splited = text.lower().split(" ")
#     return splited[0][0] == splited[1][0]
#
# print(animal_crackers('Levelheaded lama'))


# def makes_twenty(n1,n2):
#     return sum([n1,n2]) == 20 or 20 in [n1,n2]
#
#
# print(makes_twenty(10,20))

# def old_macdonald(name):
#     return name[:3].capitalize() + name[3:].capitalize()
#
# print(old_macdonald('macdonald'))


# def master_yoda(text):
#     splited = text.split(" ")
#     return " ".join(splited[::-1])
#
# print(master_yoda('I am home'))

# def almost_there(n):
#     return (n >= 90 and n <= 110) or (n >= 190 and n <= 210)
#     #
#     # if n >= 90 and n <= 110:
#     #     return True
#     # elif n >= 190 and n <= 210:
#     #     return True
#     # else:
#     #     return False
#
#
# print(almost_there(90))
# print(almost_there(104))
#
# print(almost_there(150)) #false
# print(almost_there(209))

def has_33(nums = []):
    nums = [str(num) for num in nums]
    return "33" in "".join(nums)


def has_33(nums = []):
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
#
# print(has_33([1, 3, 3]))
#
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# def paper_doll(text):
#     return "".join([l * 3 for l in text])
#
#
# print(paper_doll('Mississippi'))
# # MMMiiissssssiiippppppiii
# # MMMiiissssssiiissssssiiippppppiii


"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""

# def blackjack(a,b,c):
#     tot = sum([a,b,c])
#     if tot > 21 and 11 in [a,b,c]:
#          tot -= 10
#     if tot <= 21:
#         return tot
#     else:
#         return 'Bust'

# def blackjack(a,b,c):
#     tot = sum([a,b,c])
#     if tot <= 21:
#         return tot
#     if tot > 21 and 11 in [a,b,c]:
#          tot -= 10
#     if tot > 21:
#         return 'Bust'
#     else:
#         return tot

#
# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

"""
SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14

"""

def summer_69(nums):
    # tmp_arr = []
    # for n in nums:
    #     if n >= 6 and n <= 9:
    #         continue
    #     tmp_arr.append(n)
    tmp_arr = [num for num in nums if num < 6 or num > 9]
    return sum(tmp_arr)

# print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))

print(summer_69([2, 1, 6, 9, 11]))
#
# print("spy")
#
# def spy_game(nums):
#     tmp = [n for n in nums if n in [0,7]]
#     return tmp == [0,0,7]
#
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,5,0]))
# print([0,0,7] == [0,0,7])


#  check if given number is prime
def check_prime(n):
    if n < 2:
        return False
    else:
        multiples = []
        for num in range(n-1,1,-1):
            if n % num == 0:
                multiples.append(num)

        return len(multiples) == 0

print(check_prime(15))

#  return a list of prime numbers
def prime_nums_list(nums):
    tmp = []
    for n in nums:
        if n < 2:
            continue
        else:
            composits = []
            for num in range(n-1,1,-1):
                if n % num == 0:
                    composits.append(num)

            if len(composits) == 0:
                tmp.append(n)

    return tmp

print(prime_nums_list(range(0,101)))


# returns the number of prime numbers that exist up to and including a given number
def count_primes(p_num):
    tmp = []
    for n in range(p_num + 1):
        if n < 2:
            continue
        else:
            composits = []
            for num in range(n - 1, 1, -1):
                if n % num == 0:
                    composits.append(num)

            if len(composits) == 0:
                tmp.append(n)

    return len(tmp)

print(count_primes(100))
