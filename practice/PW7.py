import math
import random

from practice_7_functions import *


def task1():
    numbers = readfloat("task1.txt")

    print(f"a) {sum(numbers)}")

    b = 1
    for i in numbers:
        b *= i
    print(f"b) {b}")

    c = 0
    for i in numbers:
        c += i * i
    print(f"c) {c}")

    print(f"d) {abs(sum(numbers))}\t{b ** 2}")
    print(f"f) {numbers[-1]}")


def task2():
    numbers = readfloat("task2.txt")
    print(f"a) {max(numbers)}")
    print(f"b) {min(numbers)}")
    print(f"c) {max([item for item in numbers if abs(item) % 2 != 0])}")
    print(f"d) {min(numbers) + max(numbers)}")
    print(f"e) {numbers[0] - numbers[-1]}")


def task3():
    numbers = readfloat("task1.txt")

    print(f"a) {len([item for item in numbers if item % 2 == 0])}")
    print(f"b) {len([item * 2 for item in numbers if item % 2 == 0])}")
    print(
        f"c) {len([item for item in numbers if item % 2 != 0 and int(math.sqrt(item)) * int(math.sqrt(item)) == item])}")


def task4():
    f1 = open("f1.txt", "r+")
    f2 = open("f2.txt", "r+")
    buffer = open("f3.txt", "w+")

    buffer.write(f1.read())  # write info to a buffer file
    buffer.seek(0)  # set cursor position at the beginning of a file

    f1.seek(0)  # set cursor position at the beginning of a file
    f1.truncate(0)  # clear the file
    f1.write(f2.read())  # write new data

    f2.seek(0)  # set cursor position at the beginning of a file
    f2.truncate(0)  # clear the file
    f2.write(buffer.read())  # write new data

    f1.close()
    f2.close()
    buffer.close()


def task5():
    f1 = open("Task5/f1.txt", "r+")
    f2 = open("Task5/f2.txt", "r+")
    f3 = open("Task5/f3.txt", "r+")
    f4 = open("Task5/f4.txt", "r+")
    f5 = open("Task5/f5.txt", "r+")

    f1d = readall_and_clear(f1)
    f2d = readall_and_clear(f2)
    f3d = readall_and_clear(f3)
    f4d = readall_and_clear(f4)
    f5d = readall_and_clear(f5)

    f1.write(f5d)
    f2.write(f4d)
    f3.write(f1d)
    f4.write(f2d)
    f5.write(f3d)

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()


def task6():
    with open("Task6/f1.txt", "w") as file:
        file.write("12abcdef34")

    with open("Task6/f1.txt", "r") as file:
        symbols = file.read()
        if symbols[0].isdigit() and symbols[1].isdigit():
            print(str(symbols[0] + symbols[1]))
        else:
            print("Nothing")


def task7():
    path = "Task6/f.txt"
    pathg = "Task6/g.txt"
    write(path, list(range(101)))

    numbers = readint(path)

    l = list()
    l.append("Evens:\n" +
             ", ".join([str(item) for item in numbers if item % 2 == 0]) + "\n")
    l.append("Divisible by 3 and nit divisible by 7:\n" +
             ", ".join([str(item) for item in numbers if item % 3 == 0 and item % 7 != 0]) + "\n")
    l.append("Perfect squares:\n" +
             ", ".join(
                 [str(item) for item in numbers if int(math.sqrt(item)) * int(math.sqrt(item)) == item]) + "\n")
    print(l)
    write(pathg, l)


def task8():
    path = "Task8/fibb.txt"

    write(path, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    with open(path, "r+") as file:
        nums = file.read().split(" ")[-2:]
        n = int(nums[0]) + int(nums[1])

        file.write(f" {n}")


def task9():
    path1 = "Task9/f.txt"
    path2 = "Task9/g.txt"
    write(path1, "Biba Bim Boba")

    file1 = open(path1, "r")
    file2 = open(path2, "w")

    file2.write(file1.read().lower())

    file1.close()
    file2.close()


def task10():
    path = "Task10/horner.txt"
    write(path, "5 4 3 2 1")

    n = float(input("Enter a value: "))

    coeffs = readfloat(path)
    coeffs.reverse()

    res = 0
    for i in range(0, len(coeffs)):
        res += n ** (i) * coeffs[i]

    print(res)


def task11():
    path = "Task11/f.txt"
    pathg = "Task11/g.txt"
    pathh = "Task11/h.txt"

    write(path, "1 2 3 4 5 6 7 8 9 10")

    numbers = readint(path)

    write(pathg, listtostring([item for item in numbers if item % 2 == 0]))
    write(pathh, listtostring([item for item in numbers if item % 2 != 0]))


def task12():
    path = "Task12/f.txt"
    pathg = "Task12/g.txt"

    write(path, "abcdefghklmoprsqBIBA")

    write(pathg, readstring(path)[::-1])


def task13():
    path = "Task13/f.txt"
    pathg = "Task13/g.txt"
    pathh = "Task13/g.txt"

    write(path, "Biba")
    write(pathg, "Boba")

    write(pathh, readstring(path) + readstring(pathg))


def task14():
    pathf = "Task14/f.txt"
    pathg = "Task14/g.txt"

    write(pathf, "1 2 3 3 4 9 9 5 6 7 7 8 9 9 9 9 9 9")
    numbers = remove_duplicates(readint(pathf))

    write(pathg, numbers)

    # def task15():
    #     pathf = "Task15/f.txt"
    #     pathg = "Task15/g.txt"
    #
    #     write(pathf, list(range(-10, 10)))
    #
    #     numbers = readint(pathf)
    #
    #     file = open(pathg, 'w')
    #
    #     sign = 1
    #     i = -1
    #     count = 0
    #     max_count = 2
    #     indexes_buffer = [0] * max_count
    #
    #     def lower(x):
    #         return x < 0
    #
    #     def greater(x):
    #         return x >= 0
    #
    #     while i + 1 < len(numbers):
    #         i += 1
    #
    #         comparator = greater if sign == 1 else lower
    #
    #         if comparator(numbers[i]):
    #             if count + 1 == max_count:
    #                 indexes_buffer[count] = i
    #
    #                 for j in indexes_buffer:
    #                     file.write(f"{numbers[j]} ")
    #
    #                 for j in indexes_buffer[::-1]:
    #                     del numbers[j]
    #
    #                 sign *= -1
    #                 i = -1
    #                 count = 0
    #
    #             else:
    #                 indexes_buffer[count] = i
    #                 count += 1
    #
    #     file.close()


def lower(x):
    return x < 0


def greater(x):
    return x >= 0


def task15():
    pathf = "Task15/f.txt"
    pathg = "Task15/g.txt"

    write(pathf, list(range(-10, 10)))

    numbers = readint(pathf)

    file = open(pathg, "w")

    sign = 1
    i = -1
    count = 0
    max_count = 2
    indexes_buffer = [0] * max_count

    while i + 1 < len(numbers):
        i += 1

        comparator = greater if sign == 1 else lower

        if comparator(numbers[i]):
            if count + 1 == max_count:
                indexes_buffer[count] = i

                for j in indexes_buffer:
                    file.write(f"{numbers[j]} ")

                for j in indexes_buffer[::-1]:
                    del numbers[j]

                sign *= -1
                i = -1
                count = 0

            else:
                indexes_buffer[count] = i
                count += 1

    file.close()


def task16():
    pathf = "Task16/f.txt"
    pathg = "Task16/g.txt"

    write(pathf, list(range(-20, 20)))

    numbers = readint(pathf)
    numbers_copy = numbers.copy()

    file = open(pathg, "w")

    sign = 1
    i = -1
    count = 0
    max_count = 5
    indexes_buffer = [0] * max_count

    while i + 1 < len(numbers_copy):
        i += 1

        comparator = greater if sign == 1 else lower

        if comparator(numbers_copy[i]):
            if count + 1 == max_count:
                indexes_buffer[count] = i

                for j in indexes_buffer:
                    file.write(f"{numbers_copy[j]} ")

                for j in indexes_buffer[::-1]:
                    del numbers_copy[j]

                sign *= -1
                i = -1
                count = 0

            else:
                indexes_buffer[count] = i
                count += 1

    file.write('\n')

    numbers_copy = numbers.copy()
    max_count = 20
    indexes_buffer = [0] * max_count

    while i + 1 < len(numbers_copy):
        i += 1

        comparator = greater if sign == 1 else lower

        if comparator(numbers_copy[i]):
            if count + 1 == max_count:
                indexes_buffer[count] = i

                for j in indexes_buffer:
                    file.write(f"{numbers_copy[j]} ")

                for j in indexes_buffer[::-1]:
                    del numbers_copy[j]

                sign *= -1
                i = -1
                count = 0

            else:
                indexes_buffer[count] = i
                count += 1

    file.close()


def task17():
    pathf = "Task17/f.txt"
    pathg = "Task17/g.txt"

    write(pathf, [random.randint(0, 100) for i in range(0, 100 * 2)])

    numbers = readint(pathf)
    with open(pathg, "w") as file:
        i = 1

        while True:
            hundred = numbers[(i - 1) * 100:i * 100]
            if len(hundred) < 100:
                break

            file.write(f"{max(hundred)} ")
            i += 1


def task18():
    path = "Task18/f.txt"

    write(path, "Biba boba bom bim bam")

    with open(path, "a") as file:
        file.write("end")


def task19():
    pathf = "Task19/f.txt"
    pathg = "Task19/g.txt"
    pathh = "Task19/h.txt"

    write(pathf, "Bam bim boba biba")
    write(pathg, "Bub bim bac brick biba")

    fdata = readstring(pathf).split()
    gdata = readstring(pathg).split()
    write(pathh, [item for item in fdata if item in gdata])


def task20():
    pathf = "Task20/f.txt"
    pathg = "Task20/g.txt"

    write(pathf, "biba boba bam bim badam pam pam bam")

    content = readstring(pathf)

    with open(pathg, "w") as file:
        for i in range(len(content)):
            if content[i] == "a":
                if i - 1 >= 0:
                    file.write(content[i - 1])
                if i + 1 < len(content):
                    file.write(content[i + 1])


def task20_v2():
    pathf = "Task20_v2/f.txt"
    pathg = "Task20_v2/g.txt"

    write(pathf, "bbbbbbbb a cdf dhtergnmj")

    content = readstring(pathf)

    first_a = content.find("a")

    write(pathg, content[:first_a] + content[first_a + 1:])


task16()