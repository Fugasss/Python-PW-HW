import math
import re


def readnumbers(path: str, cond, converter) -> list:
    l = list()
    with open(path, "r") as file:
        l = [converter(item) for item in file.read().split(" ") if cond(item)]
        print(l)

    return l


def readfloat(path: str) -> list:
    return readnumbers(path, lambda x: re.match("-?[0-9]+.?[0-9]*", x), lambda x: float(x))


def readint(path: str) -> list:
    return readnumbers(path, lambda x: re.match("-?[0-9]+", x), lambda x: int(x))


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


def readData(f) -> str:
    s = f.read()
    f.seek(0)
    f.truncate(0)
    return s


def task5():
    f1 = open("Task5/f1.txt", "r+")
    f2 = open("Task5/f2.txt", "r+")
    f3 = open("Task5/f3.txt", "r+")
    f4 = open("Task5/f4.txt", "r+")
    f5 = open("Task5/f5.txt", "r+")

    f1d = readData(f1)
    f2d = readData(f2)
    f3d = readData(f3)
    f4d = readData(f4)
    f5d = readData(f5)

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
    with open("Task6/f.txt", "w") as file:
        file.write(str(list(range(101))).replace(",", "")[1:-1])

    numbers = readint("Task6/f.txt")

    with open("Task6/g.txt", "w") as file:
        l = list()

        l.append("Evens:\n" +
                 ", ".join([str(item) for item in numbers if item % 2 == 0]) + "\n")
        l.append("Divisible by 3 and nit divisible by 7:\n" +
                 ", ".join([str(item) for item in numbers if item % 3 == 0 and item % 7 != 0]) + "\n")
        l.append("Perfect squares:\n" +
                 ", ".join([str(item) for item in numbers if int(math.sqrt(item)) * int(math.sqrt(item)) == item]) + "\n")

        print(l)

        file.writelines(l)

def task8():
    path = "Task6/fibb.txt"
    with open(path, "w") as file:
        file.write(str([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]).replace(",", "")[1:-1])

    with open(path, "r+") as file:
        nums =file.read().split(" ")[-2:]
        n = int(nums[0]) + int(nums[1])

        file.write(f" {n}")


def task9():
    path1 = "Task9/f.txt"
    path2 = "Task9/g.txt"
    with open(path1, "w") as file:
        file.write("Biba Bim Boba")

    file1 = open(path1, "r")
    file2 = open(path2, "w")

    file2.write(file1.read().lower())

    file1.close()
    file2.close()


def task10():
    pass