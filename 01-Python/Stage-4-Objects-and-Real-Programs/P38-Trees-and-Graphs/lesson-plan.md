# P38 · Trees and Graphs

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P38-Trees-and-Graphs.pptx`

_Data structures for hierarchies and networks – and the algorithms that explore them_

## Learning goals
- Describe trees, binary trees and binary search trees
- Insert into and traverse a BST (in-order, pre-order, post-order)
- Represent a graph with an adjacency list (dictionary)
- Explore graphs with breadth-first and depth-first search, and find shortest paths

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What is a queue?  
   **Answer:** A FIFO structure – first in, first out
2. What is a stack?  
   **Answer:** A LIFO structure – last in, first out
3. What's a recursive function's base case?  
   **Answer:** The case answered directly that stops the recursion

## Slide outline & tutor notes

**3. Trees**

**4. Binary search tree (BST)**  
Draw it on paper as you insert. Then ask what happens if you insert 1,2,3,4,5 in order (it becomes a linked list – O(n). Balanced trees fix that – A-level+).

**5. Traversals**

**6. Graphs: nodes + edges, any shape**

**7. Breadth-first search: shortest path**  
Satnavs use Dijkstra's algorithm / A* – weighted versions of this idea. Dijkstra is A-level; A* is how game enemies path-find.

**8. Draw it**

**9. Trees and graphs quiz**
- What's the top node of a tree called? → **The root**
- In a BST, where do smaller values go? → **The left subtree**
- Which traversal of a BST gives sorted output? → **In-order**
- BFS uses which data structure? → **A queue**
- Which finds the shortest path in an unweighted graph, BFS or DFS? → **BFS**

## 🏠 Take-home project: Folder Tree Explorer
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your computer's folders ARE a tree. Write recursive tree functions that explore a real folder.

**Milestones**
1. Write `build_tree(path)` that returns a nested dict: `{"name": ..., "size": ..., "children": [...]}` (use `os.listdir`, `os.path.isdir`, `os.path.getsize`)
2. `print_tree(node, depth)` prints it with indentation like the `tree` command (└── and ├──)
3. `total_size(node)` adds up every file underneath a folder (recursion!)
4. `find(node, name)` returns the path to the first file with that name, or None
5. Run it on your Python course folder and print the 5 biggest files

**Stretch:** Use a queue (BFS) to print the tree level by level instead, and compare it with your recursive (DFS) version.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### BST class  (★★☆ core)
File: `exercises/ex1_bst_class.py`

Wrap the BST in a class with `insert`, `contains`, `min`, `max`, `height` and `in_order` (returning a list). Insert 1,000 random numbers and check `in_order()` equals sorted(set(numbers)).

### Maze solver  (★★☆ core)
File: `exercises/ex2_maze_solver.py`

A maze is a 2D list of strings: `#` wall, `.` path, `S` start, `E` end. Treat each open cell as a graph node with up/down/left/right neighbours. Use BFS to find the shortest path and print the maze with the path marked `*`.

### Six degrees of separation  (★★★ stretch)
File: `exercises/ex3_six_degrees.py`

Build a friendship graph (an adjacency list of at least 15 people – real or invented). Write: `degrees(a, b)` using BFS, `friends_of_friends(a)` suggestions, and `is_connected()` using DFS. Then find the two people furthest apart.

## Optional extras (if he wants more)
- Turn the maze solver into a pygame visualisation where you can watch BFS spread out
- Read about Dijkstra's algorithm – what's different when edges have weights?
