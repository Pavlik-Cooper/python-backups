import datetime
import pytz

# a = 5
# b = -6
# a -= -6
# print(a)  # - and - gives +

class Account():

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.transaction_list = [(Account._current_time(), balance)]

    def withdraw(self, amount):
        # disallow 0 and negative withdrawals
        # (0 < -5) == False
        # (0 < 0) == False
        if 0 < amount <= self.__balance:
            self.__balance -= amount                   # convert to negative
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            return print("Funds unavailable!")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            self.show_balance()

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount >= 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                # convert back to positive
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


alan = Account("ALan", 800)

#  alan object doesn't have  __balance attribute until we assign it on line 56
# (when __balance is called from inside the class it refers to _Account__balance)

alan.__balance = 200
print(alan.__balance)

alan.deposit(100)
alan.withdraw(200)
alan.withdraw(200)
alan.show_transaction()

alan._Account__balance = 0
alan.show_balance()

print(alan.__dict__)