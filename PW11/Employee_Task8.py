from datetime import datetime


class Employee_Task8:
    def __init__(self, surname, salary, birthdate: datetime):
        self.surname = surname
        self.salary = salary
        self.birthdate = birthdate

    def __str__(self):
        return f'{self.surname} {self.salary} {self.birthdate}'

    def __del__(self):
        del self.surname
        del self.salary
        del self.birthdate

    def calculateAge(self):
        today = datetime.today()
        dy = today.year - self.birthdate.year
        dm = today.month - self.birthdate.month
        dd = today.day - self.birthdate.day

        if dm < 0:
            dy += 1
        elif dm == 0 and dd <= 0:
            dy += 1

        print(f"{self.surname}'s age is {dy}")
        return dy

    def daysBefore50(self):
        if self.calculateAge() >= 50:
            print(f"{self.surname} is already 50 years old")
            return

        print(f"{(datetime(self.birthdate.year + 50, self.birthdate.month, self.birthdate.day) - datetime.today()).days} days before 50 y.o.")


# task 2
d = [Employee_Task8("Biba", 25000, datetime(2000, 5, 12))]

for i in d:
    print(i)
    i.calculateAge()
    i.daysBefore50()
    print(i)
    print()
