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
    n = int(input('Enter number n (0 <= n <= 1000)'))

    if n == 0:
        print("Ноль")
    if n == 1000:
        print("Тысяча")
        return

    result = ''

    h = int(n / 100)
    t = int(n / 10 % 10)
    o = int(n % 10)

    hundreds = {
        1: 'сто',
        2: 'двести',
        3: 'триста',
        4: 'четыреста',
        5: 'пятьсот',
        6: 'шестьсот',
        7: 'семьсот',
        8: 'восемьсот',
        9: 'девятьсот'
    }
    tens = {
        0: 'десять',
        1: 'одиннадцать',
        2: 'двенадцать',
        3: 'тринадцать',
        4: 'четырнадцать',
        5: 'пятнадцать',
        6: 'шестнадцать',
        7: 'семндацтать',
        8: 'восемнадцать',
        9: 'девятнадцать'
    }
    mtens = {
        2: 'двадцать',
        3: 'тридцать',
        4: 'сорок',
        5: 'пятьдесят',
        6: 'шестьдесят',
        7: 'семьдесят',
        8: 'восемьдесят',
        9: 'девяносто'
    }
    mones = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять'
    }

    if h > 0:
        result += hundreds[h] + ' '

    if t == 1:
        result += tens[o] + ' '
    else:
        result += mtens[t] + ' ' + mones[o] + ' '

    print(result)


def task7():
    n = int(input('Enter number n: '))

    tenge = int(n / 100)
    tiyns = n % 100

    print('{} тенге {:02d} тиин'.format(tenge, tiyns))


# Functions for tasks 8-10
def isdigit(char: str) -> bool:
    return char.isdigit()


def isletter(char: str) -> bool:
    return char.isalpha()


def issymbol(char: str) -> bool:
    return char in "*+-"


def findgroups(text, compare) -> list:
    a = list()
    start = 0
    end = 0
    for i in range(1, len(text)):
        if compare(text[i - 1]) and compare(text[i]):
            end = i + 1
        elif not compare(text[i - 1]) and compare(text[i]):
            start = i
        elif compare(text[i - 1]) and not compare(text[i]):
            if end - start > 1:
                a.append(text[start:end])
                start = i + 1

    return a


def task8():
    text = input()

    if text.find('one') != -1:
        print('В тексте есть слово "one"')
    else:
        print('В тексте нету слова "one"')

    if len(findgroups(text, isletter)) > (len(findgroups(text, isdigit)) + len(findgroups(text, issymbol))):
        print("TRUE")
    else:
        print("FALSE")


def task9():
    text = input()
    letters = findgroups(text, isletter)
    amountOfF = 0
    beginEndOccurenceCount = 0

    for i in range(0, len(letters)):
        if i >= 3:
            break

        amountOfF += letters[i].count('f')

    for i in letters:
        if i[0] == i[-1]:
            beginEndOccurenceCount += 1

    print(f'The amount of the "f" in the first three groups of letters: {amountOfF}')
    print(f'The amount of groups of letters that begin and end with the same letter: {beginEndOccurenceCount}')


def task10():
    text = input()

    groupsWithTwiceA = []

    for i in findgroups(text, isletter):
        if i.count('a') >= 2:
            groupsWithTwiceA.append(i)

    longestNumbersGroup = ''

    for i in findgroups(text, isdigit):
        if len(i) > len(longestNumbersGroup):
            longestNumbersGroup = i

    print(f'1) {groupsWithTwiceA}')
    print(f'2) {longestNumbersGroup}')


def task11():
    text = input()

    if (not text[0].islower() or
            text[0].islower() and not isdigit(text[len(findgroups(text, isletter)[0])])):
        print(text)
        return

    firstgroupofnumbers = findgroups(text, isdigit)[0]

    start = text.find(firstgroupofnumbers)
    l = len(firstgroupofnumbers)

    text = text[:start] + '*' * l + text[start + l:]

    print(text)


def task12():
    text = input()

    def makepostfix(value: str) -> str:
        i = -1
        txt = ''
        while i + 1 < len(value):
            i += 1

            if value[i] == '(':
                end = value.find(')', i)
                txt += makepostfix(value[i + 1:end])
                i += end - i + 1

            if value[i].isdigit():
                txt += value[i]

            if value[i] in '+-/*':
                if i + 1 < len(value) and value[i + 1] == '(':
                    end = value.find(')', i + 1)
                    txt += makepostfix(value[i + 2:end])
                    txt += value[i]
                    i += end - (i + 1) + 1
                else:
                    txt += value[i + 1] + value[i]
                    i += 1

        return txt

    print(makepostfix(text))


task12()
