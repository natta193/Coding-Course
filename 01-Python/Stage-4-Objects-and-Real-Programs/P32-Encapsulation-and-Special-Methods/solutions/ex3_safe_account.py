import datetime

class BankAccount:
    interest_rate = 0.02

    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0.0
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    def __record(self, kind, amount):
        self.__history.append((datetime.date.today(), kind, amount, self.__balance))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.__record("deposit", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__record("withdraw", amount)

    def add_interest(self):
        interest = round(self.__balance * BankAccount.interest_rate, 2)
        self.__balance += interest
        self.__record("interest", interest)

    def statement(self):
        print(f"Statement for {self.owner}")
        for date, kind, amount, bal in self.__history:
            print(f"{date}  {kind:9} {amount:8.2f}  balance {bal:8.2f}")

acc = BankAccount("Sam")
acc.deposit(100)
acc.withdraw(30)
acc.add_interest()
acc.statement()
try:
    acc.balance = 1_000_000
except AttributeError as e:
    print("Nice try:", e)
