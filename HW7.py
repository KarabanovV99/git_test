import math

x = float(input())
y = float(input())
c = 0
for i in range(math.ceil(x), math.floor(y) + 1):
    if i % 5 == 0:
        c += i
print(c)
