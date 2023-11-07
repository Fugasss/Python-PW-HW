# Create a list of your favorite musicians
def task1():
    musicians = ['Michael Jackson', 'Egor Letov']


# Create a dictionary containing various data about you: height, favorite color, favorite actor, etc.
def task2():
    info = {
        'name': 'Konstantin',
        'height': 171,
        'weight': 72,
        'favourite color': 'black'
    }


# Write a program that asks the user for their weight, favorite color, or actor and returns the result of the
# dictionary created in the previous task.
def task3():
    info = {
        'name': 'Unknown',
        'height': 0.,
        'weight': 0.,
        'favourite color': 'None'
    }

    for k in info.keys():
        info[k] = input(f'Enter your {k}: ')


# Create a dictionary linking your favorite musicians to a list of your favorite songs written by them.
def task4():
    musician_songs = {
        'Michael Jackson': ['Billie Jean', 'Smooth Criminal', 'Beat It', "They Don't Care About Us"],
        'Egor Letov': ['Всё идёт по плану', 'Отряд не заметил потери бойца', 'Убивать']
    }


def max_dct(*dicts:dict)->dict:
    new_dict = {}

    for d in dicts:
        for k in d:
            if new_dict.get(k, -1) < d[k]:
                new_dict[k] = d[k]

    return new_dict


def sum_dct(*dicts:dict)->dict:
    new_dict = {}

    for d in dicts:
        for k in d:
            new_dict.update({k:new_dict.get(k, 0) + d[k]})

    return new_dict


# There are a number of dictionaries with intersecting keys (values are positive numbers). Write 2 functions
# that do the following operations with an array of dictionaries:
# The 1st function max_dct(*dicts) forms a new dictionary according to the rule:
# If there are duplicate keys in the source dictionaries, we select the maximum among their values and assign
# this key (for example, dictionary_1 has the key “a” with the value 5, and dictionary_2 has the key “a”, but
# with the value 9. Choose the maximum value, t i.e. 9, and assign the key “a” in the already new dictionary).
# If the key is not repeated, then it is simply transferred with its value to the new dictionary (for example, the
# key “c” was found only in one dictionary, while others do not. Therefore, we transfer this key along with its
# value to the new dictionary). We return the generated dictionary.
# The 2nd function sum_dct(*dicts) sums the values of duplicate keys. The values of the other keys remain
# the same. (Operations are carried out similar to the first function, but not the maxima are taken, but the
# sums of the values of the keys of the same name). The function returns the generated dictionary
def task5():
    d1 = {
        'a' : 3,
        'b' : 7,
        'c' : 10
    }
    d2 = {
        'a' : 9,
        'c' : 3,
        'd' : 1
    }

    print(max_dct(d1,d2))
    print(sum_dct(d1,d2))


task5()