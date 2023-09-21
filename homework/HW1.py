from math import sqrt, atan, cos, sin, tan, e, pi, log, factorial, radians

g = 9.81
G = 6.67E-11


def task1():
    x = float(input())
    y = float(input())
    z = float(input())

    a = (sqrt(abs(x - 1)) - (abs(y) ** (1. / 3.))) / (1 + (x ** 2) / 2 + (y ** 2) / 4)
    b = x * (atan(z) + (e ** (-(x + 3))))

    print(f'a: {a}\tb: {b}')


def task2():
    x = float(input())
    y = float(input())
    z = float(input())

    a = (3 + e ** (y - 1)) / (1 + x ** (2) * abs(y - tan(z)))
    b = 1 + abs(x - y) + ((y - x) ** (2)) / (2) + (abs(y - x) ** (3)) / (3)

    print(f'a: {a}\tb: {b}')


def task3():
    x = float(input())
    y = float(input())
    z = float(input())

    a = (1 + y) * ((x + y / (x ** 2 + 4)) / (e ** (-x - 2) + 1 / (x ** 2 + 4)))
    b = (1 + cos(y - 2)) / ((x ** 4) / 2 + sin(z) ** 2)

    print(f'a: {a}\tb: {b}')


def task4():
    x = float(input())
    y = float(input())
    z = float(input())

    a = y + x / (y ** 2 + abs(x ** 2 / (y + x ** (3) / 3)))
    b = 1 + tan(z / 2) ** 2

    print(f'a: {a}\tb: {b}')


def task5():
    x = float(input())
    y = float(input())
    z = float(input())

    a = (2 * cos(x - pi / 6)) / (1 / 2 + sin(y) ** 2)
    b = 1 + (z ** 2)/(3 + z ** (2) / 5)

    print(f'a: {a}\tb: {b}')


def task6():
    x = float(input())
    y = float(input())
    z = float(input())

    a = (1 + sin(x + y) ** 2) / (2 + abs(x - 2 * x / (1 + x ** (2) * y ** (2)))) + x
    b = cos(atan(1 / z)) ** 2

    print(f'a: {a}\tb: {b}')


def task7():
    x = float(input())
    y = float(input())
    z = float(input())

    a = log(abs((y - sqrt(abs(x))) * (x - y / (z + x ** (2) / 4))))
    b = x - x ** (2) / factorial(3) + x ** (5) / factorial(5)

    print(f'a: {a}\tb: {b}')


def task8():
    a = float(input())

    area = sqrt(3) / 4 * a ** 2

    print(f"Area of equilateral triangle is {area}")


def task9():
    l = float(input())

    t = 2 * pi * sqrt(l / g)

    print(f'The period of oscillations of a pendulum with length {l} is {t} s')


def task10():
    m1 = float(input())
    m2 = float(input())
    r = float(input())

    f = G * (m1 + m2) / (r ** 2)

    print(f'The force of attraction between bodies is {f} N')


def task11():
    c = float(input())
    a = float(input())

    b = sqrt(c ** 2 - a ** 2)
    r = (a + b - c) / 2

    print(f'the second leg = {b}\tthe radius of inscribed circle = {r}')


def task12():
    v1 = float(input())
    v2 = float(input())
    a1 = float(input())
    a2 = float(input())
    s = float(input())

    k = (a1 + a2)
    h = (v1 + v2)

    D = h ** 2 + 2 * k * s
    t = 0

    if D < 0:
        print("Invalid input!")
        return

    if D == 0:
        t = -h / k
    elif D > 0:
        sD = sqrt(D)
        t1 = (-h + sD) / k
        t2 = (-h - sD) / k

        if t1 > 0:
            t = t1
        else:
            t = t2

    print(t)


def task13():
    l = [int(item) for item in input("Enter numbers: ").split(' ')]

    s = (l[0] + l[-1]) * len(l) / 2

    print(f"Sum of arithmetic progression: {s}")


def task14():
    c = float(input())
    d = float(input())

    cd = c * d
    x1 = max(-cd, cd)
    x2 = min(-cd + 3, cd + 3)

    cx13 = c * x1 ** 3
    dx22 = d * x2 ** 2

    v = cx13 + dx22

    result = abs((sin(abs(v - cd)) ** 3) / ((v - x1) ** 2 + 3.14)) + tan(v - x1)

    print(result)


def task15():
    a = float(input())
    b = float(input())
    c = sqrt(a ** 2 + b ** 2)
    area = a * b / 2

    print(f"Hypotenuse: {c}\tArea: {area}")


def task16():
    p = 1000

    v1 = float(input())
    t1 = float(input())
    v2 = float(input())
    t2 = float(input())

    m1 = p * v1
    m2 = p * v2
    v = v1 + v2
    t = (m1 * t1 + m2 * t2) / (m1 + m2)

    print(f"Volume: {v} m^3 \tTemperature: {t} *C")


def task17():
    n = int(input())
    r = float(input())

    x = (2 * r) / tan(radians(180 / n))
    p = round(n * x, 2)
    print(f"Perimeter: {p}")
