while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("That's not a number!")

try:
    result = 10 / age
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Always runs")
