def in_order(node):          # left, root, right
    if node:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)

def pre_order(node):         # root, left, right
    if node:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)

in_order(root)    # 20 30 40 50 60 70 80  <- sorted!
print()
pre_order(root)   # 50 30 20 40 70 60 80
