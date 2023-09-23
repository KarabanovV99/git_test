x = float(input())
y = float(input())
c = 0
for i in range(int(x), int(y) + 1):
    if i % 5 == 0:
        c += i
print(c)