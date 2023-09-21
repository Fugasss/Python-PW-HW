import math as math


def findRoots(a, b, c):
    D = b ** 2 - 4 * a * c

    hasRoots = True

    if D < 0:
        print("There are no valid roots!")
        hasRoots = False
        return (hasRoots, None, None)
    elif D == 0:
        x = (-b) / (2 * a)
        print(f'Root = {x}')
        return (hasRoots, x, None)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        print(f"Root 1 = {x1}\tRoot 2 = {x2}")
        return (hasRoots, x1, x2)


def task1():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())

    if a <= b <= c <= d:
        a = b = c = d = max(a, b, c, d)
    elif a > b > c > d:
        pass
    else:
        a = a ** 2
        b = b ** 2
        c = c ** 2
        d = d ** 2

    print(f"a {a}\tb {b}\tc {c}\td {d}")


def task2():
    x = float(input())
    y = float(input())

    if x < 0 and y < 0:
        x = abs(x)
        y = abs(y)
    elif (x < 0 <= y) or (x >= 0 > y):
        x = x + 0.5
        y = y + 0.5
    elif x > 0 and y > 0 and 0.5 <= x <= 2.0 and 0.5 <= y <= 2.0:
        x /= 10
        y /= 10

    print(f"x={x}\ty={y}")


def task3():
    x = float(input())
    y = float(input())
    z = float(input())

    if x < y + z:
        print("There is no triangle")
        return
    else:
        a_deg = math.degrees(math.sin(x / y))
        b_deg = math.degrees(math.sin(x / z))
        c_deg = math.degrees(math.sin(y / z))
        if 0 < a_deg < 90 and 0 < b_deg < 90 and 0 < c_deg < 90:
            print("Acute-angled")
        else:
            print("Not acute-angled")


def task4():
    a = float(input())
    b = float(input())
    c = float(input())

    findRoots(a, b, c)


def task5():
    h = float(input())

    a = math.sqrt((abs(math.sin(8 * h)) + 17) / (1 - math.sin(4 * h) * math.cos((h ** 2) + 18)) ** 2)
    b = 1 - math.sqrt(3 / (3 + abs(math.tan(a * (h ** 2)) - math.sin(a * h))))
    c = a * (h ** 2) * math.sin(b * h) + b * (h ** 3) * math.cos(a * h)

    findRoots(a, b, c)


def task6():
    a1 = float(input())
    b1 = float(input())
    c1 = float(input())
    a2 = float(input())
    b2 = float(input())
    c2 = float(input())

    (hasRoots1, x1, x2) = findRoots(a1, b1, c1)
    (hasRoots2, x3, x4) = findRoots(a2, b2, c2)
    if not hasRoots1 or not hasRoots2:
        return

    if x1 == x3 or (x2 is not None and x1 == x4):
        print(f"The first root of the system is {x1}")

    if (x2 is not None and x2 == x3) or (x2 is not None and x4 is not None and x2 == x4 ):
        print(f"The second root of the system is {x2}")
