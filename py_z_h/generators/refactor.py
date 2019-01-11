def smallest_com2(a,b):
    a_mults = []
    b_mults = []
    a,b = sorted([a,b])

    def func():
        nonlocal i
        for i in range(1, i):
            a_mults.append(a * i)
            b_mults.append(b * i)

        multiples = sorted(set(a_mults).intersection(set(b_mults)))
        return multiples

    def check(m):
        truths = []
        for num in range(a + 1, b + 1):
            flag = m % num == 0
            truths.append(flag)
        return len(truths) > 0 and all(truths)

    def filter_custom(func,arr):
        for n in arr:
            if func(n):
                return [n]
        return []


    i = 100000
    multiples = []
    while not filter_custom(check,multiples[::-1]):
        multiples = func()
        i = i+100000
    else:
        nums = filter_custom(check,multiples)

    return nums

print(smallest_com2(1,13))