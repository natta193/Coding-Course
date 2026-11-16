def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    raise ValueError(f"Unknown operator {op}")

while True:
    first = input("First number (or quit): ")
    if first == "quit":
        break
    try:
        a = float(first)
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))
        print("=", calculate(a, op, b))
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError as e:
        print("Oops:", e)
