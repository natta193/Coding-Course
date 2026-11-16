def rpn(expression):
    stack = []
    for token in expression.split():
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(a / b)
        else:
            stack.append(float(token))
    return stack.pop()

print(rpn("3 4 + 2 *"))          # 14.0
print(rpn("5 1 2 + 4 * + 3 -"))  # 14.0
