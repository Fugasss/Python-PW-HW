from math import sqrt

def task1():
    a = float(input())
    b = float(input())

    sum = a + b
    dif = a - b
    prod = a * b

    print(f'Sum: {sum}\tDif: {dif}\tProduct: {prod}')

def task2():
    x = float(input())
    y = float(input())

    result = (abs(x) - abs(y)) / (1 + abs(x*y))

    print(result)

def task3():
    a = float(input())

    volume = a**3
    area = a**2 * 6

    print(f'Area: {area}\tVolume: {volume}')

def task4():
    a = float(input())
    b = float(input())

    mean = (a+b)/2
    geo_mean = sqrt(a*b)

    print(f"Arithmetic mean: {mean}\tGeometric mean: {geo_mean}")

def task5():
    a = abs(float(input()))
    b = abs(float(input()))

    mean = (a + b) / 2
    geo_mean = sqrt(a * b)

    print(f"Arithmetic mean: {mean}\tGeometric mean: {geo_mean}")



task1()
task2()
task3()
task4()
task5()