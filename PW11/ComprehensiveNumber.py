import math


class ComprehensiveNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def magnitude(self):
        m = math.sqrt(self.re * self.re + self.im * self.im)
        print(f"Magnitude = {m}")

    def indeg(self):
        c = math.atan(self.im / self.re)
        print(f"In degrees = {math.degrees(c):.2f}°")


numbers = [
    ComprehensiveNumber(2, 3),
    ComprehensiveNumber(4, 55),
    ComprehensiveNumber(1, 32),
    ComprehensiveNumber(3, 70)
]

for i in numbers:
    i.magnitude()
    i.indeg()
    print()
