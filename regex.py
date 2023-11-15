import re
#import easygui as gui


# 1
def encode_symbol(symbol: chr, offset: int) -> chr:
    return chr(ord(symbol) + offset)


print(encode_symbol('a', 3))

# 2


def encode_str(value: str, offset: int) -> str:
    output = ''
    for i in value:
        output += encode_symbol(i, offset)


print(encode_str('Bib bub', 1))


# 3
def encode_file(input_file_path: str, output_file_path: str, key: int) -> None:
    data = ''
    with open(input_file_path, 'r') as file:
        data = file.read()

    with open(output_file_path, 'w') as file:
        file.write(encode_str(data, 3))


# # 4
# def make_application():
#     input_file = gui.fileopenbox(msg=None, title=None)
#     key = gui.integerbox(msg="", title=" ")
#
#     output_file = gui.filesavebox(msg=None, title=None)
#
#
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
            value = "<strong>" + value + "<\strong>"

        output.append(value)

    print(' '.join(output))


task5()
