n = int(input("3-digit number: "))
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
print(f"Hundreds: {hundreds}, tens: {tens}, units: {units}")
print(f"Digit sum: {hundreds + tens + units}")
