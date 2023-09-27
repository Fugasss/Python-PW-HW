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
    for i in range(0.1, 10, 0.1):
        result *= (1 + math.sin(i))


def task11():
    x = float(input())

    result = 0
    sign = 1

    for i in range(1, 14, 2):
        result += sign * (x ** i) / (math.factorial(i))
        sign *= - 1

    print(result)


def task12():
    x = float(input())
    a = float(input())
    n = int(input())

    result = (x + a) ** 2

    for i in range(0, n):
        result += (result + a) ** 2

    result += a

    print(result)


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


def task18():
    def v(i):
        if i == 3:
            return 1.5
        elif i < 3:
            return 0

        return (i + 1) / (i * i + 1) * (v(i - 1)) - v(i - 2) * v(i - 3)

    n = int(input())

    print(v(n))


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


def task21():
    def a(i):
        if i <= 1:
            return 1

        return a(i-2) + a(i-1) / (2 ** (i - 1))

    result = 1

    for i in range(0, 15):
        result *= a(i)

    print(result)
