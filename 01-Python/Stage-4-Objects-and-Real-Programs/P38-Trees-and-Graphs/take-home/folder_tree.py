# TAKE-HOME PROJECT: Folder Tree Explorer
# After lesson P38 (Trees and Graphs) - about 1–2 hours, in chunks over the next few days.
#
# Your computer's folders ARE a tree. Write recursive tree functions that explore a real
# folder.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Write build_tree(path) that returns a nested dict: {"name": ..., "size": ...,
#          "children": [...]} (use os.listdir, os.path.isdir, os.path.getsize)
#   [ ] 2. print_tree(node, depth) prints it with indentation like the tree command (└── and
#          ├──)
#   [ ] 3. total_size(node) adds up every file underneath a folder (recursion!)
#   [ ] 4. find(node, name) returns the path to the first file with that name, or None
#   [ ] 5. Run it on your Python course folder and print the 5 biggest files
#
# Stretch: Use a queue (BFS) to print the tree level by level instead, and compare it with
# your recursive (DFS) version.
#
# Bring it to the next session - working or stuck, both are fine.

import os

def build_tree(path):
    pass
