import json

class Cat:
    def __init__(self, name, slug, age):
        self.name = name
        self.slug = slug
        self.age = age
        self.claws = None

    def meow(self):
        print(f"Meow {self.name}")


cat = Cat("Іван", "Ivan", 2)


# print(json.dumps([c.__dict__], indent=4))


with open("data.json", "w") as file:
    json.dump(cat.__dict__, file, indent=4, ensure_ascii=False)  # for cyrillic ensure_ascii

with open("data.json", "r") as file:
    obj = json.load(file)
    print(obj == cat.__dict__)
    print(obj)



