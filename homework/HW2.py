import math as math


class Vec2:
    def __init__(self, xv, yv):
        self.x = xv
        self.y = yv

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


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


def area(v1, v2, v3):
    A = (v2 - v1).length()
    B = (v3 - v1).length()
    C = (v3 - v2).length()

    p = (A + B + C) / 2

    return round(math.sqrt(p * (p - A) * (p - B) * (p - C)), 3)


def task10():
    v1 = Vec2(float(input()), float(input()))
    v2 = Vec2(float(input()), float(input()))
    v3 = Vec2(float(input()), float(input()))
    vi = Vec2(float(input()), float(input()))

    s = area(v1, v2, v3)
    s1 = area(v1, v2, vi)
    s2 = area(v1, v3, vi)
    s3 = area(v2, v3, vi)

    print(f'S: {s}\t s1 = {s1}\ts2={s2}\ts3={s3}')

    if s == (s1 + s2 + s3):
        print("Point inside")
    else:
        print("Point outsider")


def can_fit(a, b, c, d):
    return (a / c >= 1 and b / d >= 1) or (a / d >= 1 and b / c >= 1)


def task11():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())

    if can_fit(a, b, c, d):
        print("Can fit")
    else:
        print("Can't fit")


def task12():
    a = float(input())
    b = float(input())
    c = float(input())
    x = float(input())
    y = float(input())

    if can_fit(a, b, x, y) or can_fit(a, c, x, y) or can_fit(b, c, x, y):
        print("Can fit")
    else:
        print("Can't fit")


def task13():
    def f(x):
        if -2 <= x < 2:
            return x * x

        return 4

    a = float(input())

    print(f(a))


def task14():
    def f(x):
        v = x * x + 4 * x + 5
        if x <= 2:
            return v

        return 1 / v

    a = float(input())

    print(f(a))


def task15():
    def f(x):
        if x <= 0:
            return 0
        elif 0 < x <= 1:
            return x

        return x ** 4

    a = float(input())

    print(f(a))


def task16():
    def f(x):
        if x <= 0:
            return 0
        elif 0 < x <= 1:
            return x * x - x

        return x * x - math.sin(math.pi * x * x)

    a = float(input())

    print(f(a))


def task17():
    def f1(x):
        if x <= 0:
            return -x

        return - x * x

    def f2(x):
        if x <= -1:
            return -1 / (x * x)
        if -1 < x <= 2:
            return x * x

        return 4

    a = float(input())

    print(f1(a))
    print(f2(a))


def task18():
    def f1(x):
        if x <= 0:
            return abs(x + 1)

        return abs(x - 1)

    def f2(x):
        if x <= 1:
            return abs(x)
        elif 1 < x <= 2:
            return 1

        return -2 * x + 5

    a = float(input())

    print(f1(a))
    print(f2(a))


def task19():
    def f1(v):  # circle
        if v.length() <= 1:
            return "Inside the unit circle"

        return "Not in the unit circle"

    def f2(v):  # ring
        if 0.5 <= v.length() <= 1:
            return "Inside the ring"

        return "Not in the ring"

    def f3(v):  # square
        if abs(v.x) <= 1 and abs(v.y) <= 1:
            return "Inside the square"

        return "Not in the square"

    vec = Vec2(float(input()), float(input()))

    print(f1(vec))
    print(f2(vec))
    print(f3(vec))


def task20():
    def f1(v):  # rhombus
        lf = abs(v.x) - 1
        uf = -abs(v.x) + 1

        if uf >= v.y >= lf:
            return "Inside the rhombus"

        return "Not in the rhombus"

    def f2(v):  # crystal
        lf = 2 * abs(v.x) - 1
        uf = -2 * abs(v.x) + 1

        if uf >= v.y >= lf:
            return "Inside the crystal"

        return "Not in the crystal"

    def f3(v):  # blob
        inthecircle = v.length() <= 1
        lf = -(v.x + 2) / 2
        uf = (v.x + 2) / 2

        if inthecircle and lf <= v.y <= uf:
            return "In the blob"

        return "Not in the blob"

    vec = Vec2(float(input()), float(input()))

    print(f1(vec))
    print(f2(vec))
    print(f3(vec))


task20()
