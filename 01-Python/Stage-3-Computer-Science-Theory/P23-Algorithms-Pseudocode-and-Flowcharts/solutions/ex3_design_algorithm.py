# Pseudocode:
# FOR EACH coin IN coins (largest first)
#     WHILE amount >= coin
#         add coin to result; amount ← amount - coin
# OUTPUT result

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def make_change(pence, coins=COINS):
    result = []
    for coin in coins:
        while pence >= coin:
            result.append(coin)
            pence -= coin
    return result

print(make_change(388))          # [200, 100, 50, 20, 10, 5, 2, 1]
print(make_change(6, [4, 3, 1])) # [4, 1, 1] – 3 coins, but 3+3 is only 2!
# Greedy works for UK coins but NOT for every coin system.
