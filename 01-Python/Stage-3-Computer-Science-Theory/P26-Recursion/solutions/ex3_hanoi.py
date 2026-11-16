moves = 0

def hanoi(n, source, target, spare):
    global moves
    if n == 0:
        return
    hanoi(n - 1, source, spare, target)
    moves += 1
    print(f"Move disc {n} from {source} to {target}")
    hanoi(n - 1, spare, target, source)

hanoi(4, "A", "C", "B")
print(f"{moves} moves")                    # 2^n - 1 = 15
print(f"64 discs: {2**64 - 1:,} moves")   # ~585 billion years at 1 move/sec
