import re
import string

import easygui as gui


# 1
def encode_symbol(symbol: chr, offset: int) -> chr:
    if symbol.isupper():
        return chr((ord(symbol) - 65 + offset) % 26 + 65)

    if symbol.islower():
        return chr((ord(symbol) - 97 + offset) % 26 + 97)

    return symbol


# print(encode_symbol('c', 104))

# 2
def encode_str(value: str, offset: int) -> str:
    output = ''
    for i in value:
        output += encode_symbol(i, offset)

    return output


# print(encode_str('Bib bub', 1))


# 3
def encode_file(input_file_path: str, output_file_path: str, key: int) -> None:
    data = ''
    with open(input_file_path, 'r') as file:
        data = file.read()

    with open(output_file_path, 'w') as file:
        file.write(encode_str(data, 3))


# 4
def make_application() -> None:
    input_file = gui.fileopenbox(msg=None, title=None)
    key = gui.integerbox(msg="Enter offset", title=" ")
    output_file = gui.filesavebox(msg=None, title=None)

    encode_file(input_file, output_file, key)


# make_application()


# 5
def task5():
    inp = input('Enter a text: ')

    words = inp.split(' ')
    word_count = dict()

    for i in set(words):
        word_count[i] = words.count(i)

    output = []

    for w in words:
        value = w
        if word_count[w] > 1:
            value = r"<strong>" + value + r"<\strong>"

        output.append(value)

    print(' '.join(output))


# task5()


# 6
def task6():
    pattern = r"^(?:0[1-9]|[1-2][0-9]|30)\/(?:0[1-9]|1[0-2])\/(?:202[0-3]|20[0-1][0-9]|1[0-9]{3})$"

    inps = ['12/12/2024', '12/10/2000', '15/13/1001', '05/12/1991']

    req = '\n'.join(inps)

    matches = re.findall(pattern, req, re.M)

    print("Input:\n", req)
    print("Valid dates:", matches)


# task6()


# 7
def task7():
    inp = input("Enter ipv4 strings in any format: ").split(' ')

    inp = '\n'.join(inp)

    ipv4_10d = r"\b(?:(?:25[0-5]|(?:2[0-4]|1\d|[1-9]|)\d)\.?\b){4}"
    ipv4_16d = r'\b(?:0x[0-9a-fA-F]{1,2}(?:\.|$)){4}'
    ipv4_8d = r'\b(?:0[0-7]{1,3}(?:\.|$)){4}'

    ipv4_16 = r'\b0x(?:[0-9A-F]{2}){4}'
    ipv4_8 = r'\b(?:[0-3][0-7]{2}){4}'

    print('IPv4_10_dots:', re.findall(ipv4_10d, inp))
    print('IPv4_8_dots:', re.findall(ipv4_8d, inp))
    print('IPv4_16_dots:', re.findall(ipv4_16d, inp))
    print('IPv4_16_no_dots:', re.findall(ipv4_16, inp))
    print('IPv4_8_no_dots:', re.findall(ipv4_8, inp))


# 8
def task8():
    inp = input().split(' ')

    seq = ''
    last = inp[0]

    for i in inp[1:]:
        print(i)
        if i > last:
            seq += i
            last = i
        else:
            break

    print('The first sequence of distinct ascendant characters:', seq)


# task8()


# 9
def task9():
    inp = "Aboba's      cat likes     to lick its       own BALLS!    It is the worst thing   that    cat made in its life."

    words = inp.split()

    res = ''

    for w in words:
        if w[-1] == string.punctuation:
            res += w + '  '
        else:
            res += w + ' '

    res = res.rstrip()

    print(res)


# task9()


# 10
def task10():
    inp = 'bim boba bam bim bom boa bib    bim boba bam bim bom boa bic b ara ara ara ora ora ora muda muda muda'

    lines = []

    for i in range(0, int(len(inp) / 32) + 1):
        a = inp[i * 32:(i + 1) * 32]

        if len(a) != 0:
            lines.append(a.split())

    for l in lines:
        print(l)

    res = set()

    for j in range(len(lines) - 1):
        ml1 = len(lines[j])
        ml2 = len(lines[j + 1])
        min_len = ml1 if ml1 < ml2 else ml2
        for i in range(min_len):
            l1 = lines[j][i]
            l2 = lines[j + 1][i]

            if l1 == l2:
                res.add(lines[j][i])

    print(res)


# task10()


# 11
def task11():
    pass


# 12
def task12():
    inp = input('Enter a text')
    pattern = input('Enter a word')

    print(pattern, 'was found' if re.search(pattern, inp) is not None else "wasn't found")


# 13
def task13():
    pass


# 14
def task14():
    pattern = r'\b\w*?lo'

    inp = 'biba boba bil zhil hello i dilo'

    print(re.findall(pattern, inp))


# 15
def task15():
    numbers = '\n'.join(['+7 (707) 777 77 77', '+77073242323', '+7 (707) 777-77-77'])

    print(re.findall(r'^(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}(?:\s|-)?(?:\d{2}(?:\s|-)?){2}$', numbers, re.M))


# task15()

# 16
def task16():
    inp = input('Enter a text: ')
    delimiters = [item for item in input('Enter delimiters: ') if not item.isspace()]

    for d in delimiters:
        print(inp.split(d))


# task16()

# 17
def task17():
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="home.css">
    <link rel="stylesheet" href="common.css">
    <title>Home</title>
</head>
<body>
<div class="main_body">
    <div class="main_header background">
        <h1>Home</h1>
    </div>
    <div class="main_info background">
        <p>My name is Konstantin. I study in IITU and doing this laboratory work for ICT.</p>
        <p>You can press the buttons to change current page.</p>
    </div>
    <div class="main_nav background">
        <iframe class="nav_frame" src="navigation.html" title="Navigation"></iframe>
    </div>
    <div class="main_floor background">
        <b>Made by Grishin Konstantin</b>
    </div>
</div>
</body>
</html>
    '''

    res = re.findall(r'(?:<.*>)+.+(?:<\/.*>)+', html, re.M)
    res = [re.findall(r'(?<=>)[a-zA-z .]+(?=<)', item, re.M)[0] for item in res]

    print(res)


#task17()


# 18
def task18():

    text = 'Завтрак в 09:00'

    print(re.findall(r'(?:[0-1][0-9]|2[0-3]):(?:0[0-9]|[1-5][0-9])', text))


#task18()