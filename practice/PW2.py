def task1():
    def interval(x):
        if 1 < x < 3:
            print('\t', x)

    a = float(input())
    b = float(input())
    c = float(input())

    interval(a)
    interval(b)
    interval(c)


def task2():
    x = float(input())
    y = float(input())

    a = (x + y) / 2
    b = 2 * x * y

    if x < y:
        x = a
        y = b
    else:
        x = b
        y = a

    print(f"X: {x}\tY: {y}")


def task3():
    a = float(input())
    b = float(input())
    c = float(input())

    if a > 0:
        a = a ** 2
    if b > 0:
        b = b ** 2
    if c > 0:
        c = c ** 2

    print(f'a : {a}\tb: {b}\tc: {c}')


def task4():
    x = float(input())
    y = float(input())
    z = float(input())

    if (x + y + z) < 1:
        mn = min(x, y, z)
        if x == mn:
            x = (y + z) / 2
        elif y == mn:
            y = (x + z) / 2
        else:
            z = (x + y) / 2
    else:
        mn = min(x, y)
        if x == mn:
            x = (y + z) / 2
        else:
            y = (x + z) / 2

    print(f'x: {x}\ty: {y}\tz: {z}')
