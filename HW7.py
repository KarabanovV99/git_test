x = int(input())
y = int(input())
c = 0
for i in range(x, y +1):
    if i % 5 == 0:
        c = c + i
print(c)