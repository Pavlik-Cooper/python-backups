class Animal():

    tail = True

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"My name is {self.name} and my weight is {self.weight}"

    def __len__(self):
        return len(self.__str__())

    def __del__(self):
        print("I was removed")



class Dog(Animal):

    def __init__(self,name,weight,spots):
        Animal.__init__(self,name,weight)
        self.spots = spots

    def describe(self):
        if self.spots and Dog.tail:
            print(f"i have spots and tail")
        else:
            print("i don't have spots or tail")





bob = Dog("boby",12,True)

describe_method = getattr(bob,'describe',None)
print(callable(describe_method))

bob.describe()
Dog.describe(bob) # // i have spots and tail

print(bob)          # __str__()
print(len(bob))     # __len__()

del bob    # // I was removed
# print(help(slice))
