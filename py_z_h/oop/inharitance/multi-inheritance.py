class Aquatic:

  def __init__(self, name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"Hi! I am {self.name} of the sea!"


class Ambulatory:

  def __init__(self, name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"HI! I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):

  def __init__(self, name):
    print("PENGUIN INIT!")
    super().__init__(name=name)

    # if you want to call both __init__ as well as change the order

    # Aquatic.__init__(self, name=name)
    # Ambulatory.__init__(self, name=name)



captain_cook = Penguin("Captain Cook")


print(captain_cook.swim())
print(captain_cook.walk())

print(captain_cook.greet())

print(Penguin.__mro__)
# print(Penguin.mro())
# help(Penguin)




















