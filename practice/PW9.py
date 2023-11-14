import random
from collections import namedtuple


# 1
def tuple_sort(tpl: tuple) -> tuple:
    for i in tpl:
        if not isinstance(i, int):
            return tpl

    return tuple(sorted(tpl, key=lambda x: x))


# print(tuple_sort((1, 2, 3, 1, 0, 9, 8)))
# print(tuple_sort((1, 4, 5, 3, 2, 8, 6, 0, 1, "asdgb")))
# print(tuple_sort((1, 4, 5, 3, 2, 8, 6.0, 0, 1, 5)))


# 2
def slicer(tpl: tuple, el) -> tuple:
    if tpl.count(el) == 0:
        return tuple()
    if tpl.count(el) == 1:
        t = list(tpl)
        t.remove(el)
        t.insert(el, 0)
        return tuple(t)

    t = list(tpl)
    t.remove(el)
    t.remove(el)

    t.insert(0, el)
    t.insert(len(t), el)

    return tuple(t)


# print(slicer((1, 3, 4, 5, 6, 2, 1, 5, 3, 5, 7, 3, 5, 7, 8), 3))


# 3
def sieve(lst: list) -> tuple:
    return tuple(sorted(set(lst), reverse=True))


# print(sieve([1, 6, 4, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 4, 5, 7]))


# 4
def del_from_tuple(tpl: tuple, el) -> tuple:
    if tpl.count(el) == 0:
        return tpl

    t = list(tpl)
    t.remove(el)

    return tuple(t)


# print(del_from_tuple((1, 2, 3, 4, 5, 6, 7, 8), 3))


# 5
student = namedtuple(typename="student", field_names=['name', 'age', 'grade', 'city'])


def good_students(students: tuple):
    avg = 0.0

    for i in students:
        avg += i.grade

    avg /= len(students)

    well_students = []

    for i in students:
        if i.grade >= avg:
            well_students.append(i.name)

    print(f"Average grade is {avg}")
    print(f"{well_students} are doing well this semester")


# good_students((
#     student("Max", 18, 4.0, "Almaty"),
#     student("Arsen", 19, 3.3, "Almaty"),
#     student("Nekolya", 19, 2.77, "Almaty"),
#     student("Nikita", 19, 3.3, "Almaty"),
#     student("Biba", 23, 3.2, "Almaty"),
#     student("Bob", 32, 2.2, "Almaty"),
#     student("Jasulan", 27, 1.9, "Almaty"),
# ))


# 6
def task6():
    athlets = [
        ("Bob", "Swimming", 5),
        ("Max", "Athletic", 2),
        ("Dex", "Throwing", 3),
        ("Joseph", "Running", 1),
        ("Jonathan", "Swimming", 1)
    ]

    for i in athlets:
        if i[1] == "Swimming":
            print(i[0], i[2])


# 7
def task7():
    skaters = [
        ("Joseph", 7.0),
        ("Jonathan", 8.0),
        ("Jenifer", 9.5),
        ("Bob", 7.5),
        ("Dex", 7.6),
        ("Max", 6.6),
    ]

    avg = 0.0
    for i in skaters:
        avg += i[1]
    avg /= len(skaters)

    for i in skaters:
        if i[1] >= avg:
            print(i[0])


# 8
def del_min_max(tpl: tuple) -> tuple:
    tpl = del_from_tuple(tpl, max(tpl))
    tpl = del_from_tuple(tpl, min(tpl))
    return tpl


# print(del_min_max((1,2,3,4,5,6,7)))


# 9
def task9():
    t = (1, 2, 3, 4, 5, 6, 7)

    tl = list(t)

    mni = tl.index(min(t))
    mxi = tl.index(max(t))

    (tl[mni], tl[mxi]) = (tl[mxi], tl[mni])

    t = tuple(tl)

    print(t)


# 10
def task10():
    t = (1, 2, 3)

    sum_of_sqr = 0.0
    for i in t:
        if i > 0:
            sum_of_sqr += i * i
    mean = sum_of_sqr / len(t)
    print(mean)


def task11():
    contacts = [
        ("John", 31),
        ("Max", 19),
        ("Arsen", 18),
        ("Nelay", 20)
    ]

    inp = input()
    found = False
    for i in contacts:
        if i[0] == inp:
            print(i[0], "is", i[1])
            found = True

    if not found:
        print("Not found")


# 12
def task12():
    inp = input()

    l = [int(i) for i in inp.split() if i.isdigit()]
    t = tuple(l)

    print("List:", l)
    print("Tuple:", t)


# 13
def task13():
    names = ["Max", "Arsen", "Bob", "Bib"]
    ages = [19, 20, 22, 18]
    speciality = ["IT", "Journalism", "Rabotyaga", "Clown"]
    group = ["IT2-2121", "JR1-2020", "RAB1-1905", "CLW2-2202"]

    students = []

    for i in range(0, min(len(names), len(ages), len(speciality), len(group))):
        students.append((names[i], ages[i], speciality[i], group[i]))

    print(students)


# 14
def task14():
    queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 10, 10]
    queue.insert(7, "Qalaisyn ?")
    print(queue)

    copy = queue[6]
    queue.pop(6)
    queue.insert(0, copy)
    print("Queue after moving 6th element to the beginning:", queue)

    repeated_values = len(queue) - len(set(queue))
    print("Number of repeated values:", repeated_values)

    queue.sort(key=lambda x: str(x))
    print("Sorted queue:", queue)


# 15
def task15():
    subject_names = ["Mathematics", "Physical Education", "Calculus"]
    grades = [45, 100, 85]
    students = ["Arsen", "Max", "Miras", "Bob"]
    queue = students.copy()

    def print_info():
        print("-" * (20 * 3 + 10))
        print("| {:^20s} | {:^20s} | {:^20s} |".format("Subject Name", "Subject Grade", "Student"))
        print("-" * (20 * 3 + 10))
        for i in range(len(subject_names)):
            print(f"| {subject_names[i]:<20} | {grades[i]:<20} | {queue[i]:<20} |")
        print("-" * (20 * 3 + 10))

    print("Before")
    print_info()

    if 45 in grades:
        for i in range(len(grades)):
            if grades[i] == 45:
                grades[i] = random.randint(51, 59)

    print("\nAfter")
    print_info()


def task16():
    different = ["one", "two", "one", "1",
                 1, "5", 1, "1", 123, 321,
                 123, 321, 90, "Python", "python",
                 "Python", "lecture", 4]

    s = set(different)

    unique = []

    for i in s:
        if different.count(i) == 1:
            unique.append(i)

    print("Number of unique values:", len(unique))
    print(unique)

    set1 = {"C#", "C", "C++", "Java"}
    set2 = {"Python", "Rust", "Go"}
    set3 = set1.union(set2)

    print("\n\nResulting set:", set3)

    subset = {"C", "Go"}
    if subset.issubset(set3):
        print(subset, "is a subset of", set3)
    else:
        print(subset, "is not a subset of", set3)

    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {6, 7, 8, 9}

    min_1 = min(numbers1)
    max_1 = max(numbers1)
    min_2 = min(numbers2)
    max_2 = max(numbers2)

    print("\n\n1) Min:", min_1, '\t', "Max", max_1)
    print("2) Min:", min_2, '\t', "Max", max_2)

    max_set = numbers1 if numbers1 > numbers2 else numbers2
    print("Maximal set:", max_set)


def task17():
    words = {
        'apple': ['A fruit', 'A company'],
        'phone': ['A device to make calls'],
        'pool': ['A place water contains', 'A set of elements']
    }

    inp = input('Enter a word:')

    if inp.lower() in words.keys():
        print()
        print(inp)
        c = 1
        for i in words.get(inp.lower()):
            print(f'\t({c})', i)
            c += 1

    print("\n\n")

    people = {
        1: ("Arsen", "2004 03 11", "+7 (707) 303 30 30"),
        2: ("Max", "2004 07 10", "+7 (707) 404 40 40"),
        3: ("Nikita", "2004 02 27", "+7 (707) 505 50 50"),
    }

    inp = int(input('Enter an id: '))

    if inp in people.keys():
        p = people.get(inp)
        print("Name:", p[0])
        print("Birthday:", p[1])
        print("Phone:", p[2])

    print("\n\n")

    exchange = {
        "USD": 463.65,
        "RUB": 5.12,
        "YEN": 3.07
    }

    print('Available currencies:', ", ".join(exchange.keys()))

    inp = input('Enter a currency name: ').upper()

    if inp in exchange.keys():
        print(1, inp, "is", exchange.get(inp), "KZT")