import jsonpickle


class Cat:
    def __init__(self, name, slug, age):
        self.name = name
        self.slug = slug
        self.age = age
        self.claws = None

    def meow(self):
        print(f"Meow {self.name}")


cat = Cat("Іван", "Ivan", 2)


with open("json_pickle.json", "w") as file:
    frozen = jsonpickle.encode(cat)
    file.write(frozen)


with open("data.json", "r") as file:
    contents = file.read()
    obj = jsonpickle.decode(contents)
    print(obj)

