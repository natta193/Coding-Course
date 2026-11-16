height = int(input("Height in cm: "))
age = int(input("Age: "))

if height < 140:
    print("Sorry, you must be at least 140 cm.")
elif age < 12:
    adult = input("Are you with an adult? (y/n) ")
    if adult == "y":
        print("Enjoy the ride!")
    else:
        print("Under-12s need an adult.")
else:
    print("Enjoy the ride!")
