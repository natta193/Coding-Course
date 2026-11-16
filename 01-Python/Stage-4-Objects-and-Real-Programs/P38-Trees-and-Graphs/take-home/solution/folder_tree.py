import os
from collections import deque


def build_tree(path):
    node = {"name": os.path.basename(path) or path, "path": path, "children": [], "size": 0}
    if os.path.isdir(path):
        for entry in sorted(os.listdir(path)):
            if entry.startswith(".") or entry == "__pycache__":
                continue
            node["children"].append(build_tree(os.path.join(path, entry)))
    else:
        node["size"] = os.path.getsize(path)
    return node


def total_size(node):
    return node["size"] + sum(total_size(c) for c in node["children"])


def print_tree(node, prefix=""):
    kids = node["children"]
    for i, child in enumerate(kids):
        last = i == len(kids) - 1
        print(prefix + ("└── " if last else "├── ") + f"{child['name']} ({total_size(child):,} B)")
        print_tree(child, prefix + ("    " if last else "│   "))


def find(node, name):
    if node["name"] == name:
        return node["path"]
    for c in node["children"]:
        found = find(c, name)
        if found:
            return found
    return None


def all_files(node):
    if not node["children"] and node["size"]:
        return [node]
    return [f for c in node["children"] for f in all_files(c)]


def bfs_levels(root):
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        print("  " * depth + node["name"])
        queue.extend((c, depth + 1) for c in node["children"])


root = build_tree(os.path.dirname(os.path.abspath(__file__)))
print(root["name"])
print_tree(root)
print("Total:", f"{total_size(root):,} bytes")
print("Found README at:", find(root, "README.md"))
for f in sorted(all_files(root), key=lambda n: -n["size"])[:5]:
    print(f"  {f['size']:>8,}  {f['name']}")
