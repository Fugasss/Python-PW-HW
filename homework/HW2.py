import math as math
import numpy as numpy


# If there is only one root the method will return
# root as a first variable and None for the second:
# x1 = root
# x2 = None
# In case there is two roots the method will return
# both roots
# x1 = root1
# x2 = root2
# otherwise None for both will be returned
# x1 = None
# x2 = None
def find_quadratic_roots(a, b, c):
    D = b ** 2 - 4 * a * c

    if D < 0:
        return (None, None)
    elif D == 0:
        x = (-b) / (2 * a)
        return (x, None)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)


def find_biquadratic_roots(a, b, c):
    (t1, t2) = find_quadratic_roots(a, b, c)
    (x1, x2, x3, x4) = (None, None, None, None)

    if t1 is not None and t1 >= 0:
        x1 = math.sqrt(t1)
        x2 = -x1
    if t2 is not None and t2 >= 0:
        x3 = math.sqrt(t2)
        x4 = -x3

    return (x1, x2, x3, x4)


def print_roots(x1, x2):
    if x1 is None and x2 is None:
        print("There are no valid roots!")
    elif x2 is None:
        print(f'Root = {x1}')
    else:
        print(f"Root #1 = {x1}\tRoot #2 = {x2}")


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

    (x1, x2) = find_quadratic_roots(a, b, c)
    print_roots(x1, x2)


def task5():
    h = float(input())

    a = math.sqrt((abs(math.sin(8 * h)) + 17) / (1 - math.sin(4 * h) * math.cos((h ** 2) + 18)) ** 2)
    b = 1 - math.sqrt(3 / (3 + abs(math.tan(a * (h ** 2)) - math.sin(a * h))))
    c = a * (h ** 2) * math.sin(b * h) + b * (h ** 3) * math.cos(a * h)

    (x1, x2) = find_quadratic_roots(a, b, c)
    print_roots(x1, x2)


def task6():
    a1 = float(input())
    b1 = float(input())
    c1 = float(input())
    a2 = float(input())
    b2 = float(input())
    c2 = float(input())

    (x1, x2) = find_quadratic_roots(a1, b1, c1)
    (x3, x4) = find_quadratic_roots(a2, b2, c2)
    roots = [x1, x2, x3, x4]
    valid_roots = set([item for item in roots if item is not None and roots.count(item) > 1])

    print(f"Roots: {valid_roots}")


def task7():
    a = float(input())
    b = float(input())
    c = float(input())

    roots = list(find_biquadratic_roots(a, b, c))
    valid_roots = set([item for item in roots if item is not None])

    print(f"Roots: {valid_roots}")


# example input:
# -0.5
# 0
# -0.139
# 0
# 3.6
# -1
# 1
# example output:
# Points lie on the different parts of the plane
def task8():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    s = float(input())
    t = float(input())
    u = float(input())

    def line_eq(x):
        return -(s * x + u) / t

    l1 = line_eq(x1)
    l2 = line_eq(x2)

    if (y1 > l1 and y2 > l2) or (y1 < l1 and y2 < l2):
        print("Points lie on the same half of the plane")
    else:
        print("Points lie on the different parts of the plane")

# Example input:
# 3
# 4
# 0.5
# 3
# 1.7
# 1.7
# 0.4
# -2
# Example output:
# Points lie on the different parts of the plane
def task9():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())

    def line_eq(x):
        return (y4 - y3) / (x4 - x3) * (x - x3) + y3

    l1 = line_eq(x1)
    l2 = line_eq(x2)

    if (y1 > l1 and y2 > l2) or (y1 < l1 and y2 < l2):
        print("Points lie on the same half of the plane")
    else:
        print("Points lie on the different parts of the plane")


def task10():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())

    