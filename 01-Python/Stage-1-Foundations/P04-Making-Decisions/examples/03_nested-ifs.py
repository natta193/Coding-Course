has_ticket = input("Ticket? (y/n) ") == "y"
age = int(input("Age: "))

if has_ticket:
    if age >= 15:
        print("Enjoy the 15-rated film!")
    else:
        print("Sorry, too young for this one.")
else:
    print("Please buy a ticket first.")
