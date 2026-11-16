#     0 1 1 0 1 1 0 1   (109)
#   + 0 1 0 1 1 0 0 1   ( 89)
#   = 1 1 0 0 0 1 1 0   (198)
#
# Rules: 0+0=0  0+1=1  1+1=10 (carry 1)  1+1+1=11

a, b = 200, 100
total = (a + b) % 256      # 8-bit register
print(total)               # 44 – overflow!
