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

    def sort_forward(l: list) -> None:
        i = -1
        while i + 1 < len(l):
            i += 1
            j = i
            while j + 1 < len(l):
                j += 1
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]

    def sort_backward(l: list) -> None:
        i = -1
        while i + 1 < len(l):
            i += 1
            j = i
            while j + 1 < len(l):
                j += 1
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]

    sort_forward(numbers)  # subtask 2
    print(numbers)

    sort_backward(numbers)  # subtask 3
    print(numbers)


def task11():
    words = ['Australia', 'Eurasia', 'Africa', 'continent', 'land', 'North America', 'population', 'South America',
             'race', 'language']
    sens = sorted(words)
    insens = sorted(words, key=str.lower)

    print(words)
    print(sens)
    print(insens)


def task12():
    animals = ['tiger', 'bear', 'lion', 'wolf', 'fox', 'zebra', 'eagle', 'penguin', 'dog', 'cat']
    print(animals)

    animals1 = animals.copy()
    animals1.reverse()
    print(animals1)

    animals2 = animals.copy()
    animals2 = animals2[::-1]
    print(animals2)


def task13():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print([item for item in numbers if item % 2 != 0])


def task14():
    pl = 'Python'

    print([ord(item) for item in pl])


def task15():
    words = ['d@ll', 'b@ll', 'go@l', 'f@ll', '@mb@ss@dor', 'c@pit@l']
    print(words)
    print("")

    # 1st method
    words1 = []
    for word in words:
        newword = ""
        for char in word:
            if char == "@":
                newword += "a"
                continue

            newword += char
        words1.append(newword)
    print(words1)

    # 2nd method
    words2 = list(map(lambda c: c.replace("@", "a"), words))
    print(words2)

    # 3rd method
    words3 = [item.replace("@", "a") for item in words]
    print(words3)


def task16():
    numbers = [-5, 4, 0, -3, 5, -2, 8, 2, -1]
    # 1st method
    numbers1 = []
    for number in numbers:
        if number >= 0:
            numbers1.append(number)

    print(numbers1)

    # 2nd method
    numbers2 = list(filter(lambda x: x >= 0, numbers))
    print(numbers2)

    # 3rd method
    numbers3 = [item for item in numbers if item >= 0]
    print(numbers3)


def task17():
    numbers = [7, 10, 15, 56, 40, 32, 5, 12, 17, 24, 22, 53, 31]

    for number in numbers:
        s = ""

        if number % 4 == 0:
            s += "Fizz"
        if number % 5 == 0:
            s += "Buzz"

        print(number, s if s != "" else "the number is neither Fizz nor Buzz")


def task18():
    numbers = list(range(1, 9))
    print(numbers)

    l = len(numbers)
    for i in range(0, int(l / 2)):
        print(numbers[i], numbers[l - i - 1])


def task19():
    numbers = [2 * i for i in range(0, 50)]
    print(numbers)
    print(len(numbers))


def task20():
    numbers = list(range(100))

    print("To stop the program, enter 'x'")

    words = {"one",
             "two",
             "three",
             "four",
             "five",
             "six",
             "seven",
             "eight",
             "nine",
             "ten",
             "eleven",
             "twelve",
             "thirteen",
             "fourteen",
             "fifteen",
             "sixteen",
             "seventeen",
             "eighteen",
             "nineteen",
             "twenty",
             "thirty",
             "forty",
             "fifty",
             "sixty",
             "seventy",
             "eighty",
             "ninety",
             "hundred"}

    while True:
        n = input("Enter any number: ")
        if n.isdigit():
            print("Number found" if numbers.count(int(n)) != 0 else "Number not found")
            continue

        if len([item for item in n.split() if item.lower() in words]) != 0:
            print("Blin vvedi chislami :( 🤢")
        else:
            print("Chto ti panapisal 🤬🤬🤬🤬🤬🤬🤬🤬🤬")

        if n == "x":
            break
