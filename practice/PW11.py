# 1
class Date:
    def __init__(self, day, month, year):

        if year < 1:
            print("Incorrect year")

        if month not in range(1,13):
            print("Incorrect month")

        if month == 2:
            if day not in range(1, 29):
                print('Incorrect day')
        elif month in [1,3,5,7,8,10,12]:
            if day not in range(1, 32):
                print('Incorrect day')
        else:
            if day not in range(1, 31):
                print('Incorrect day')


        self.day = day
        self.month = month
        self.year = year

    def __del__(self):
        del self.day
        del self.month
        del self.year

        print(type(Date), 'deleted')

    def func1(self):
        print('Is yearleap' if self.year % 4 == 0 else "Isn't yearleap")

    def func2(self):
        pass
