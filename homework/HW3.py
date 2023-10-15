import math as math


def task1():
    n = int(input())

    result = 1

    for i in range(1, n):
        result *= (1 + 1 / (n ** 2))

    print(result)


def task2():
    n = int(input())

    result = 0

    for i in range(1, n + 1):
        s = 0
        for j in range(0, i):
            s += math.sin(j)
        result += 1 / s

    print(result)


def task3():
    n = int(input())

    result = 0

    for i in range(0, n):
        result = math.sqrt(2 + result)

    print(result)


def task4():
    n = int(input())

    result = 1

    for i in range(1, n):
        sm = 0
        cm = 0
        for j in range(1, n):
            sm += math.sin(j)
            cm += math.cos(j)
        result *= cm / sm

    print(result)


def task5():
    n = int(input())

    result = 0

    for i in range(0, n):
        result = math.sqrt(3 * (n - i) + result)

    print(result)


def task6():
    n = int(input())
    a = float(input())

    result = 0

    for i in range(0, n):
        ad = 1
        for j in range(0, n):
            ad *= (a + j)

    print(result)


def task7():
    n = int(input())
    a = float(input())

    result = 1

    for i in range(0, n):
        result *= (a + i)

    print(result)


def task8():
    n = int(input())
    a = float(input())

    result = 0

    for i in range(0, n):
        result += 1 / (a ** (2 ** n))

    print(result)


def task9():
    n = int(input())
    a = float(input())

    result = 1

    for i in range(0, n + 1):
        result *= (a - i * n)

    print(result)


def task10():
    result = 1

    for i in range(1, 101):
        result *= (1 + math.sin(i / 10))

    print(result)


def task11():
    x = float(input())

    result = 0
    sign = 1

    for i in range(1, 14, 2):
        result += sign * (x ** i) / (math.factorial(i))
        sign *= - 1

    print(result)


def task12():
    x, a = float(input()), float(input())
    n = int(input())

    for i in range(n):
        x = (x + a) ** 2
    x += a

    print(x)


def task13():
    x = float(input())

    result = 1

    for i in range(2, 65, 2):
        result *= (x - i) / (x - i - 1)

    print(result)


def task14():
    x = float(input())
    n = int(input())

    result = 0

    for i in range(1, n + 1):
        result += math.sin(x) ** i

    print(result)


def task15():
    x = float(input())
    n = int(input())

    result = 0

    for i in range(1, n + 1):
        result += math.sin(x ** i)

    print(result)


def task16():
    x = float(input())
    n = int(input())

    result = 0

    for i in range(1, n + 1):
        s = math.sin(x)
        for j in range(1, i):
            s = math.sin(s)
        result += s

    print(result)


def task17():
    def a(k):
        if k <= 0:
            return 1

        return k * a(k - 1) + 1 / k

    n = int(input())

    print(a(n))


def task17_withoutrecursion():
    n = int(input())
    a = 1
    for i in range(1, n + 1):
        a = i * a + 1 / i
    print(a)


def task18():
    def v(i):
        if i == 3:
            return 1.5
        elif i < 3:
            return 0
        return (i + 1) / (i * i + 1) * (v(i - 1)) - v(i - 2) * v(i - 3)

    n = int(input())

    print(v(n))


def task18_withoutrecursion():
    n = int(input())

    al1 = 1.5
    al2 = 0
    al3 = 0
    for i in range(4, n + 1):
        m = (i + 1) / (i * i + 1)
        a = m * al1 - al2 * al3
        al3 = al2
        al2 = al1
        al1 = a

    print(al1)


def task19():
    q = float(input())
    r = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    n = int(input())

    def x(k):
        if k <= 0:
            return c
        elif k == 1:
            return d

        return q * x(k - 1) + r * x(k - 2) + b

    print(x(n))


def task19_withoutrecursion():
    q = float(input())
    r = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    n = int(input())

    x0 = c
    x1 = d

    for i in range(2, n + 1):
        x = q * x1 + r * x0 + b
        x0 = x1
        x1 = x

    print(x1)


def task20():
    def u(i):
        if i <= 2:
            return 0

        return (u(i - 1) - u(i - 2) * v(i - 1) - v(i - 2)) / (1 + u(i - 1) ** 2 + v(i - 1) ** 2)

    def v(i):
        if i <= 2:
            return 1

        return (u(i - 1) - v(i - 1)) / (abs(u(i - 2) + v(i - 1)) + 2)

    n = int(input())

    print(v(n))


def task20_withoutrecursion():
    n = int(input())

    u1, u2 = 0, 0
    v1, v2 = 1, 1

    for i in range(3, n + 1):
        u = (u2 - u1 * v2 - v1) / (1 + u2 ** 2 + v2 ** 2)
        v = (u2 - v2) / (abs(u1 + v2) + 2)
        u1 = u2
        u2 = u
        v1 = v2
        v2 = v

    print(v2)


def task21():
    def a(i):
        if i <= 1:
            return 1

        return a(i - 2) + a(i - 1) / (2 ** (i - 1))

    result = 1

    for i in range(0, 15):
        result *= a(i)

    print(result)


def task21_withoutrecursion():
    a0, a1, result = 1, 1, 1

    for i in range(2, 15):
        a = a0 + a1 / (2 ** (i - 1))
        a0 = a1
        a1 = a
        result *= a

    print(result)


# Vi = Vi-1 + Vi-2
# Vi-2 = Vi-1
# Vi-1 = Vi