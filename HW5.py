<<<<<<< HEAD
x = float(input())
y = float(input())
if x == 0 or y == 0:
    print("нулевая координата")
elif x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x > 0 and y < 0:
    print("4 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
elif x == 0:
    print("ось ординат")
elif y == 0:
    print("ось абсцис")
=======
x = int(input())
y = int(input())
if x == 0 or y == 0:
    print("точка лежит на оси")
elif x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x > 0 and y < 0:
    print("4 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
else:
    print("erorr")
>>>>>>> d763727929bf4d2ac5acea7ebe8e8adeb8287758
