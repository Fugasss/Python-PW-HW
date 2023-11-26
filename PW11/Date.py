from MyMath import *

class Date:
    def __init__(self, day, month, year):

        if year < 1:
            print("Incorrect year")

        if month not in range(1, 12 + 1):
            print("Incorrect month")
            month = repeat(month, 1, 12 + 1)

        if month == 2:
            if day not in range(1, 29 + 1):
                print('Incorrect day')
                day = repeat(day, 1, 29 + 1)
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            if day not in range(1, 31 + 1):
                print('Incorrect day')
                day = repeat(day, 1, 31 + 1)
        else:
            if day not in range(1, 30 + 1):
                print('Incorrect day')
                day = repeat(day, 1, 30 + 1)

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

    def isYearLeap(self) -> bool:
        print('Is yearleap' if self.year % 4 == 0 else "Isn't yearleap")
        return self.year % 4 == 0

    def increaseDate(self, daysCount: int):
        d = self.day
        m = self.month
        y = self.year

        if self.month == 2:
            if self.year % 4 == 0:
                d = (self.day + daysCount) % (29 + 1)
                d += (1 if d < self.day else 0)
            else:
                d = (self.day + daysCount) % (28 + 1)
                d += (1 if d < self.day else 0)
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            d = (self.day + daysCount) % (31 + 1)
            d += (1 if d < self.day else 0)
        else:
            d = (self.day + daysCount) % (30 + 1)
            d += (1 if d < self.day else 0)

        if d < self.day:
            m = (self.month + 1) % (12 + 1)
            m += (1 if m < self.month else 0)
        if m < self.month:
            y += 1

        self.day = d
        self.month = m
        self.year = y

    def decreaseDate(self, daysCount: int):
        d = self.day
        m = self.month
        y = self.year

        d = (self.day - daysCount)

        if d <= 0:
            off = d
            if m == 3:
                d = 29 if self.isYearLeap() else 28
            elif m in [1, 3, 5, 7, 8, 10, 12]:
                d = 30
            else:
                d = 31

            d += off

            if m - 1 == 0:
                m = 12
                y -= 1
            else:
                m -= 1

        self.day = d
        self.month = m
        self.year = y

    def __sub__(self, other):
        if not isinstance(other, Date):
            raise TypeError()

        d = Date(self.day - other.day, self.month - other.month, self.year - other.year)

        days = 366 * d.year // 4 + 365 * (d.year - d.year // 4) + d.month

        d.decreaseDate(days)

        return d


# task 1
d = [Date(5, 2, 2004),
     Date(3, 12, 2009),
     Date(28, 10, 2000)]

for i in d:
    print(i)
    i.isYearLeap()
    i.increaseDate(5)
    print(i)
    print()

# task 6

d = [Date(5, 2, 2004), Date(3, 12, 2009), Date(28, 10, 2000)]

for i in d:
    print(i)
    i.year += 1
    i.decreaseDate(2)
    print(i)
    print()

# task 13

d = [Date(5, 2, 2004), Date(3, 12, 2009), Date(28, 10, 2000)]

for i in d:
    print(i)
    print("Number of the month and the day are", ("eqaul" if i.day == i.month else "not equal"))
    print()
