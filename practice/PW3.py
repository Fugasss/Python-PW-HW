def get_numbers():
    numbers = []

    while True:
        try:
            a = input("Enter a number: ")

            if a.lower() == "done":
                break

            a = float(a)
        except:
            print("Invalid input")
        else:
            numbers.append(a)

    return numbers


def task1():
    numbers = get_numbers()
    s = sum(numbers)
    l = len(numbers)

    print(s, l, s / l if l > 0 else 0)


def task2():
    numbers = get_numbers()
    s = sum(numbers)
    l = len(numbers)

    print(s, l, min(numbers), max(numbers))

task1()
task2()