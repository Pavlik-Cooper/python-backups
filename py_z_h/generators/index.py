a, b = 1, 1

# a, b = b, a + b  // this is identical

tmp = a
a = b
b = tmp + b



def generator():
    for n in range(5):
        yield n

# for n in generator():
#     print(n)

gen = generator()

print(next(gen))  # //  0
print(next(gen))  # //  1
print(next(gen))  # //  2
print(next(gen))  # //  3
print(next(gen))  # //  4
# print(next(gen))  # //  5 and an error StopIteration is being thrown


gen = generator()

# print(list(gen))

def gen_fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        # tmp = a
        # a = b
        # b = tmp + b
        a, b = b, a + b


print(list(gen_fib(15)))
#
# s = iter("my_crazy_str")
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
