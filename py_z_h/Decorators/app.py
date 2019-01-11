def hello():
    def greet():
        print("Greets")

    return greet

hello()()

def my_decorator(my_func):

    def wrap():
        print("Extra code before the original func")
        my_func()
        print("Extra code after the original func")

    return wrap

@my_decorator # the same as:   func_to_be_decorated = my_decorator(func_to_be_decorated)
def func_to_be_decorated():
    print("The original func code")



func_to_be_decorated()