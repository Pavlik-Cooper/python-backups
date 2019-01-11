import os
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584

arr = [1,2,3,4,[5,6,7,[8,9,10,[15,20,[25,(30,35)]]]]]

def flatten(arr,tmp = []):
    for item in arr:
        if type(item) is list or type(item) is tuple:
            flatten(item, tmp)
        else:
            tmp.append(item)
    return tmp

# print(flatten(arr))

# def fact(n):
#     res = 1
#     if n > 1:
#         for i in range(2, n+1):
#             res *= i
#     return res
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# def gen_fib(n):
#     a, b = 1,1
#     tmp = []
#     for i in range(n):
#         tmp.append(a)
#         a,b = b, a + b
#     return tmp
#
# def fib_recursion(n):
#     if n < 2:
#         return 1
#     else:
#         return fib_recursion(n-1) + fib_recursion(n-2)
#
#
# print(gen_fib(10))
# tmp = [fib_recursion(i) for i in range(10)]
# print(tmp)


# listing = os.walk(".")
# for root, directories, files in listing:
#     print(root)
#     for directory in directories:
#         print(directory)
#     for file in files:
#         print(file)
