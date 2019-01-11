import pickle

class Cat:
    def __init__(self, name, slug, age):
        self.name = name
        self.slug = slug
        self.age = age
        self.claws = None

    def meow(self):
        print(f"Meow {self.name}")


c = Cat("Іван", "Ivan", 2)

with open("data.pickle", "wb") as file:
    pickle.dump(c, file)

with open("data.pickle", "rb") as file:
    obj = pickle.load(file)
    obj.meow()
    print(obj.__dict__)