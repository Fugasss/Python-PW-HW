class FourNumbers:
    def __init__(self, a: int | float, b: int | float, c: int | float, d: int | float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def avgmean(self):
        print("Mean: {}".format((self.a + self.b + self.c + self.d) / 4))

    def max(self):
        print("Max: {}".format(max(self.a, self.b, self.c, self.d)))


numbers = [
    FourNumbers(1, 2, 3, 4),
    FourNumbers(2, 3, 4, 5),
    FourNumbers(3, 4, 5, 6)
]

for i in numbers:
    i.avgmean()
    i.max()
    print()
