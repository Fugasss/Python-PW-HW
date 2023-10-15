from math import *


def input_numbers(amount):
    n = []
    for i in range(amount):
        n.append(int(input()))

    return n


def my_sum(k, n, func):
    result = 0
    for i in range(k, n + 1):
        result += func(i)

    return result


def is_full_square(n):
    r = sqrt(n)
    return abs(r - floor(r)) < 1E-10


def is_5pow(a):
    b = 1

    while b < a:
        b *= 5

    return b == a


def is_prime(a):
    if a == 1:
        return False

    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False

    return True


def task1():
    def f(a, b, c):
        return (2 * a - b - sin(c)) / (5 + fabs(c))

    s, t = float(input()), float(input())

    result = f(t, -2 * s, 1.17) + f(2.2, t, s - t)

    print(result)


def task2():
    def g(a, b):
        return (a ** 2 + b ** 2) / (a ** 2 + 2 * a * b + 3 * b ** 2 + 4)

    s, t = float(input()), float(input())

    result = g(1.2, s) + g(t, s) - g(2 * s - 1, s * t)

    print(result)


def task3():
    def t(x):
        return (my_sum(0, 10, lambda k: (x ** (2 * k + 1)) / factorial(2 * k + 1)) /
                my_sum(0, 10, lambda k: (x ** (2 * k)) / factorial(2 * k)))

    y = float(input())

    result = (1.7 * t(0.25) + 2 * t(1 + y)) / (6 - t(y ** 2 - 1))

    print(result)


def task4():
    a, b, c = float(input()), float(input()), float(input())

    result = (max(a, a + b) + max(a, b + c)) / (1 + max(a + b * c, 1, 15))

    print(result)


def task5():
    a, b = float(input()), float(input())

    result = min(min(a, b) + (min(a * b, a + b)) ** 2, 3.14)

    print(result)


def task6():
    n, m = int(input("Enter n")), int(input("Enter m"))

    print(f"Enter {n} numbers for a")
    a = input_numbers(n)
    print(f"Enter {m} numbers for b")
    b = input_numbers(m)
    print(f"Enter 30 numbers for c")
    c = input_numbers(30)

    def l():
        if abs(min(a)) > 10:
            return min(b) + min(c)

        return 1 + (max(c)) ** 2

    print(l())


def task7():
    n = int(input("Enter n: "))
    x, y = float(input("Enter x: ")), float(input("Enter y: "))

    nums = []
    print(f"Enter a and b consequencly from {n} to 0")
    for i in range(n, 0, -1):
        nums.append(complex(float(input()), float(input())))

    result = complex(0, 0)
    xyImag = complex(x, y)

    for i in range(0, n):
        imag = nums[i]
        pimag = xyImag ** i

        result += imag * pimag

    print(result)


def task8():
    u1, u2, v1 = float(input()), float(input()), float(input())
    v2, w1, w2 = float(input()), float(input()), float(input())

    u = complex(u1, u2)
    v = complex(v1, v2)
    w = complex(w1, w2)

    result = 2 * u + (3 * u * w) / (2 + w - v) - 7

    print(result)


def task9():
    n = int(input("Enter n: "))
    print(f"Enter {n} numbers of a sequence")
    inp = input_numbers(n)

    def find_sequence(cond):
        start = 0
        end = 0
        length = 0

        for i in range(1, n):
            if cond(inp[i - 1]) and cond(inp[i]):
                end = i
            elif not cond(inp[i - 1]) and cond(inp[i]):
                start = i
            else:
                if end - start > length:
                    length = end - start

        return inp[start:end + 1]

    a = find_sequence(is_full_square)
    b = find_sequence(is_5pow)
    c = find_sequence(is_prime)

    print(f"a) {a}")
    print(f"b) {b}")
    print(f"c) {c}")


def task10():
    n = int(input("Enter n: "))
    sn = round(sqrt(n)) + 1
    b = []
    for i in range(1, n + 1):
        for j in range(0, sn):
            for k in range(j, sn):
                if j * j + k * k > i:
                    break

                if i == j * j + k * k and b.count(i) == 0:
                    b.append(i)

    print(sorted(set(b)))


def task11():
    n = int(input("Enter n: "))

    def divisors(a):
        d = []

        for i in range(1, a):
            if round(a / i - int(a / i), 5) == 0:
                d.append(i)

        return d

    perf = []
    for i in range(1, n):
        div = divisors(i)
        if sum(div) == i:
            perf.append(i)

    print(perf)


def task12():
    result = my_sum(1, 100, lambda i: my_sum(1, 50, lambda j: 1 / (i + j * j)))
    print(result)


def task13():
    result = my_sum(1, 100, lambda i: my_sum(1, 60, lambda j: sin((i ** 3 + j ** 4))))
    print(result)


def task14():
    result = my_sum(1, 100, lambda i: my_sum(i, 100, lambda j: (j - i + 1) / (i + j)))
    print(result)


def task15():
    result = my_sum(1, 100, lambda i: my_sum(1, i, lambda j: 1 / (2 * j + i)))
    print(result)


def task16():
    n = int(input("Enter n: "))

    def mul(i):
        res = 1
        for j in range(i, i * i):
            res *= j
        return res

    result = my_sum(1, n, lambda k: mul(k))
    print(result)


def task17():
    n = int(input("Enter n: "))
    result = my_sum(1, n, lambda k: 1 / factorial(k * k))
    print(result)


def task18():
    n = int(input("Enter n: "))
    result = my_sum(1, n, lambda k: (-1) ** k * factorial(2 * k * k + 1))
    print(result)


def task19():
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))
    result = my_sum(1, n, lambda k: (factorial(2 * k) + abs(x) / factorial(k ** k)))
    print(result)


def task20():
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))
    result = my_sum(1, n, lambda k: (-1) ** k * (x ** k) / factorial(factorial(k) + 1)) / factorial(n)
    print(result)


def task21():
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))
    result = my_sum(1, n, lambda k: my_sum(k, n, lambda m: (x + k) / m))
    print(result)


def task22():
    task19()


def task23():
    def h(a, b):
        return a / (1 + b * b) + b / (1 + a * a) - (a - b) ** 3

    s, t = float(input()), float(input())

    result = h(s, t) + max(h(s - t, s * t) ** 2, h(s - t, s + t) ** 4 + h(1, 1))
    print(result)

