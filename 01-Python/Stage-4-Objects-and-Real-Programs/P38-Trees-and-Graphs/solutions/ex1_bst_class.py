import random

class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _ins(node):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _ins(node.left)
            elif value > node.value:
                node.right = _ins(node.right)
            return node
        self.root = _ins(self.root)

    def contains(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def min(self):
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def height(self, node="start"):
        if node == "start":
            node = self.root
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def in_order(self):
        out = []
        def _walk(n):
            if n:
                _walk(n.left); out.append(n.value); _walk(n.right)
        _walk(self.root)
        return out

nums = [random.randint(0, 10000) for _ in range(1000)]
t = BST()
for n in nums:
    t.insert(n)
print(t.in_order() == sorted(set(nums)), t.min(), t.max(), "height", t.height())
print(t.contains(nums[0]), t.contains(-1))
