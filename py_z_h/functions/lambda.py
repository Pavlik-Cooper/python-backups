my_nums = [0,1,2,3,4,5,6]
big_nums = [100,200,300,400]

def square(n):
    return n * n

def even(n):
    return n%2 == 0

squared_nums = map(square,my_nums)
evn_nums = filter(even,my_nums)



squared_nums = map(lambda n:n * n,my_nums)
evn_nums = filter(lambda n:n % 2 == 0,my_nums)

print(list(squared_nums))
print(list(evn_nums))