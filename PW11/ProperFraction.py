class ProperFraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def inpercents(self):
        print(f"{self.num}/{self.den} in percents = {self.num / self.den * 100:.2f}%")

    def sumofdigitsindenominator(self):
        i: int = self.den
        s = 0
        while i != 0:
            s += i % 10
            i //= 10

        print(f"Sum of digits in denominator = {s}")


fractions = [
    ProperFraction(2, 3),
    ProperFraction(4, 55),
    ProperFraction(1, 32),
    ProperFraction(3, 70)
]

for i in fractions:
    i.inpercents()
    i.sumofdigitsindenominator()
    print()
