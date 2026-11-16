stack = []
stack.append("page1")    # push
stack.append("page2")
stack.append("page3")
print(stack[-1])         # peek -> page3
print(stack.pop())       # pop  -> page3
print(stack.pop())       # pop  -> page2
print(len(stack) == 0)   # is_empty -> False
