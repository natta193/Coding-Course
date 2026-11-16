def check_pin(correct_pin):
    for attempt in range(3):
        if input("PIN: ") == correct_pin:
            return True
        print("Incorrect PIN")
    return False

def deposit(balance):
    amount = float(input("Deposit amount: £"))
    if amount > 0:
        balance += amount
    return balance

def withdraw(balance):
    amount = float(input("Withdraw amount: £"))
    if amount > balance:
        print("Insufficient funds")
    elif amount > 0:
        balance -= amount
    return balance

def main():
    balance = 100.0
    if not check_pin("1234"):
        print("Card retained.")
        return
    while True:
        choice = input("1) Balance 2) Deposit 3) Withdraw 4) Quit: ")
        if choice == "1":
            print(f"Balance: £{balance:.2f}")
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
