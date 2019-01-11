class Kettle:
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    class Haha:
        def echo(self):
            print("hahahhaha")


kenwood = Kettle("Kenwood", 8.99)

print(kenwood.power_source)
kenwood.power_source = "gas"

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.power_source)

Kettle.color = "white"
hamilton.color = "blue"

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

ha = Kettle.Haha()
ha.echo()
