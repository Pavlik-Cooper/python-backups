
def test_args(*args, foo, **kwargs):
    print(args)
    print(foo)
    print(kwargs)


# test_args(1,5,6,5,foo="bar", name="paul", age=15)
test_args(*[1,5,6,5], foo="bar", **{"name":"paul","age": 15})
