def task1():
    text = input()
    text += " "

    count = 0
    start = 0
    end = 0

    for i in range(1, len(text)):
        if text[i - 1].isdigit() and text[i].isdigit():
            end = i + 1
        elif not text[i - 1].isdigit() and text[i].isdigit():
            start = i
        elif text[i - 1].isdigit() and not text[i].isdigit():

            if end - start > count:
                count = end - start
                start = i + 1

    print(count)


def task2():
    text = input()

    for i in text:
        if not (i.isalpha() or i.isspace()):
            print("True")
            break
    else:
        print("False")


def task3():
    text = input()
    nText = ''
    if text.find('*') != -1:
        for i in range(len(text)):
            if text[i] == '*':
                nText += text[i:]
                break
            if text[i].islower():
                nText += '3'
            else:
                nText += text[i]
    else:
        nText = text

    print(nText)


def task4():
    text = input()
    nText = ''
    if text.find('+') != -1:
        for i in range(len(text)):
            if text[i] == '+':
                nText += text[i:]
                break
            if text[i].islower():
                nText += '-'
            else:
                nText += text[i]
    else:
        nText = text

    print(nText)


def task5():
    text = input()
    nText = ''
    for i in range(len(text)):
        if text[i].islower():
            for j in range(i):
                nText += '.'
            nText += text[i:]
            break


    print(nText)

def task6():
    pass