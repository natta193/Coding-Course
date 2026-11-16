class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        return True

acc = BankAccount("Sam", 50)
acc.deposit(25)
acc.withdraw(100)        # Insufficient funds
print(acc.balance)       # 75
