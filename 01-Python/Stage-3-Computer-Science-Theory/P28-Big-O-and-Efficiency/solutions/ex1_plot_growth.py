import math
import matplotlib.pyplot as plt

ns = list(range(1, 101))
plt.plot(ns, [math.log2(n) for n in ns], label="log n")
plt.plot(ns, ns, label="n")
plt.plot(ns, [n * math.log2(n) for n in ns], label="n log n")
plt.plot(ns, [n * n for n in ns], label="n²")
plt.ylim(0, 1000)
plt.xlabel("n (input size)")
plt.ylabel("steps")
plt.legend()
plt.title("How algorithms grow")
plt.show()
