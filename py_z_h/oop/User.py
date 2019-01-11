class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    @classmethod
    def display_active_users(cls):
        print(f"There are currently {cls.active_users} active users")

    @classmethod
    def from_string(cls, data_str):
        fst, lst, age = data_str.split()
        return cls(fst, lst, int(age))

    def logout(self):
        User.active_users -= 1

    def __repr__(self):
        return f"User {self.first} {self.last} aged {self.age}"

User.display_active_users()
jane = User("Jane", "Doe", 18)
paul = User.from_string("Paul Rep 19")

print(jane)
print(paul)
paul.logout()
User.display_active_users()

