def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def km_to_miles(km):
    return km * 0.621371

def kg_to_stone(kg):
    return kg / 6.35029

print("1) °C→°F  2) °F→°C  3) km→miles  4) kg→stone")
choice = input("Choice: ")
value = float(input("Value: "))
if choice == "1":
    print(f"{c_to_f(value):.1f} °F")
elif choice == "2":
    print(f"{f_to_c(value):.1f} °C")
elif choice == "3":
    print(f"{km_to_miles(value):.2f} miles")
elif choice == "4":
    print(f"{kg_to_stone(value):.2f} stone")
else:
    print("Unknown choice")
