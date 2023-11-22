# 1
class Date:
    def __init__(self, day, month, year):

        if year < 1:
            print("Incorrect year")

        if month not in range(1, 13):
            print("Incorrect month")

        if month == 2:
            if day not in range(1, 29):
                print('Incorrect day')
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            if day not in range(1, 32):
                print('Incorrect day')
        else:
            if day not in range(1, 31):
                print('Incorrect day')

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return (f'{self.day}/{self.month}/{self.year}')

    def __del__(self):
        del self.day
        del self.month
        del self.year

        print(Date.__name__, 'deleted')

    def func1(self):
        print('Is yearleap' if self.year % 4 == 0 else "Isn't yearleap")

    def func2(self):
        d = self.day
        m = self.month
        y = self.year
        if self.month == 2:
            if self.year % 4 == 0:
                d = (self.day + 5) % (29 + 1)
                d += (1 if d < self.day else 0)
            else:
                d = (self.day + 5) % (28 + 1)
                d += (1 if d < self.day else 0)
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            d = (self.day + 5) % (31 + 1)
            d += (1 if d < self.day else 0)
        else:
            d = (self.day + 5) % (30 + 1)
            d += (1 if d < self.day else 0)

        if d < self.day:
            m = (self.month + 1) % (12 + 1)
            m += (1 if m < self.month else 0)
        if m < self.month:
            y += 1

        self.day = d
        self.month = m
        self.year = y



d= [Date(24, 2, 2004),Date(30, 12, 2009), Date(28, 10, 2000)]

for i in d:
    print(i)
    i.func1()
    i.func2()
    print(i)
    print()