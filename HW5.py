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
else:
    print("ось абсцис")
