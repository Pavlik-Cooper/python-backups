
class A:
    def do_smth(self):
        print("INSIDE OF A")


class B(A):
    def do_smth(self):
        print("INSIDE OF B")


class C(A):
    def do_smth(self):
        print("INSIDE OF C")


class D(B, C):
    pass
    # def do_smth(self):
    #     print("INSIDE OF D")


obj = D()
obj.do_smth()

print(D.mro())
# help(D)