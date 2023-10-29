import re
import os


def read(path: str, cond=None, converter=None) -> list:
    with open(path, "r") as file:
        l = [(converter(item) if converter is not None else item)
             for item in file.read().split(" ")
             if (cond(item) if cond is not None else True)]
        print(l)
        return l


def readstring(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


def readfloat(path: str) -> list:
    return read(path, lambda x: re.match("-?[0-9]+.?[0-9]*", x), lambda x: float(x))


def readint(path: str) -> list:
    return read(path, lambda x: re.match("-?[0-9]+", x), lambda x: int(x))


def listtostring(l: list) -> str:
    return str(l).replace(",", "")[1:-1]


def readall_and_clear(f) -> str:
    s = f.read()
    f.seek(0)
    f.truncate(0)
    return s


def write(path: str, v: list | str | int | float) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        if isinstance(v, list):
            file.write(listtostring(v))
        if isinstance(v, str):
            file.write(v)
        if isinstance(v, int) or isinstance(v, float):
            file.write(str(v))


def remove_duplicates(s: list) -> list:
    seen = set()
    return [x for x in s if not (x in seen or seen.add(x))]
