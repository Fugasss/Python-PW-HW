import random


def task1():
    numbers = [0, 2, 5, 7, 3, 1, 6, 8, 9]
    print(f'Index of "7": {numbers.index(7)}')


def task2():
    articles = ['the', 'a', 'the', 'an', 'the', 'the', '', 'a', '']
    print(f'Amount of "the": {articles.count("the")}')


def task3():
    l1 = [0] * 10
    l2 = list(range(10))


def task4():
    a = list(range(0, 10))

    # using loops
    print("using loops")
    amount1 = 0
    smallest1 = a[0]
    largest1 = a[0]
    for i in a:
        amount1 += 1
        if i < smallest1:
            smallest1 = i
        if i > largest1:
            largest1 = i

    print(amount1)
    print(smallest1)
    print(largest1)
    # using list's methods
    print("list's methods")

    amount2 = len(a)
    smallest2 = min(a)
    largest2 = max(a)

    print(amount2)
    print(smallest2)
    print(largest2)


def task5():
    l = list()
    # the 1st task
    l.append(1)

    # the 2nd task
    l.insert(0, 2)

    # the 3rd task
    l.extend([3, 4, 5])

    print(l)


def task6():
    fathers = ['James Gosling', 'Rasmus Lerdorf', 'Matthias Felleisen', 'Guido van Rossum', 'Larry Wall',
               'Bjarne Stroustrup', 'Yukihiro Matsumoto']
    print(fathers)
    # the 1st task
    fathers.pop(len(fathers) - 1)
    print(fathers)
    # the 2nd task
    fathers.pop(random.randint(1, len(fathers) - 1))
    print(fathers)

    # the 3rd task
    fathers.remove('James Gosling')
    print(fathers)

    # the 4th task
    fathers.clear()
    print(fathers)


def task7():
    cities = ['Almaty', 'Kostanay', 'Aktau', 'Shymkent', 'Semey', 'Karagandy', 'Nur-Sultan']
    print(cities)

    # the 1st method
    cities1 = cities.copy()
    print(cities1)
    # the 2nd method
    cities2 = list()
    for i in cities:
        cities2.append(i)
    print(cities2)

    # the 3rd method
    cities3 = list()
    cities3.extend(cities)
    print(cities3)


def task8():
    coffee = ['americano', 'latte', 'frappuccino', 'cappuccino', 'espresso', 'mocha']
    print(coffee)

    coffee1 = list()
    for i in range(0, len(coffee)):
        coffee1.append(coffee[len(coffee) - 1 - i: len(coffee) - i][0])

    print(coffee1)


def task9():
    fruits = ['orange', 'melon', 'apple', 'banana', 'watermelon', 'pineapple']

    s = ""
    for i in fruits:
        s += i + ", "
    print(s[0:-2])

    i = -1
    s = ""
    while i + 1 < len(fruits):
        i += 1
        s += fruits[i] + ", "
    print(s[0:-2])


def task10():
    numbers = [3, 4, 7, 1, 2, 8, 9, 5, 6]
    print(sorted(numbers))  # subtask 1

    def sort_forward(l:list)->None:
        i = -1
        while i + 1 < len(l):
            i += 1
            j = i
            while j + 1 < len(l):
                j+=1
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]

    def sort_backward(l:list)->None:
        i = -1
        while i + 1 < len(l):
            i += 1
            j = i
            while j + 1 < len(l):
                j+=1
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]

    sort_forward(numbers)   # subtask 2
    print(numbers)

    sort_backward(numbers)  # subtask 3
    print(numbers)


def task11():
    words = ['Australia', 'Eurasia', 'Africa', 'continent', 'land', 'North America', 'population', 'South America', 'race', 'language']
    sens = sorted(words, key=str.islower)
    insens = sorted(words, key=str.lower)

    print(words)
    print(sens)
    print(insens)


