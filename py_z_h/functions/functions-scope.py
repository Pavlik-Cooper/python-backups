import os

def list_directories(path):
    """  In order to manipulate variable from outer (not global) scope, one has to declare it as nonlocal.
        If a variable will be used only for reading, eg. (print(indent)),
        then there's no point using nonlocal keyword, for eg, code on line 16 (print(" " * indent + "Directory " + file))
        would perfectly work without nonlocal keyword, because we only print it. But on line 17 we're updating indent
        so python thinks we're updating local variable indent before assignment
    """
    def dir_list(d):
        nonlocal indent
        files = os.listdir(d)
        for file in files:
            curr_path = os.path.join(d, file)
            if os.path.isdir(curr_path):
                print(" " * indent + "Directory " + file)
                indent += 1
                dir_list(curr_path)
                indent -= 1
            else:
                print(" " * indent + file)

    indent = 0
    if os.path.exists(path):
        print("Directory listing of " + path + "\n")
        dir_list(path)
    else:
        print(path + " doesn't exist")


list_directories(".")


def spam1():

    def spam2():

        def spam3():
            z = " even" + y
            print("spam3 locals ", locals())
            return z

        y = " more " + x
        y += spam3()
        print("spam2 locals ", locals())
        return y

    x = "spam"
    x += spam2()
    print("spam1 locals ", locals())
    return x

# print(spam1())

# my_global = 5
#
# def test_scope():
#     my_local = 15
#     def loc_func():
#         pass
#
#     print(locals())
#
#
# print(globals())
#
# print("========")
#
# test_scope()