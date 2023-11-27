import math
from datetime import datetime


class Employee_Task11:
    def __init__(self, surname: str, position: str, salary: float):
        self.surname = surname
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'{self.surname} {self.position} {self.salary}'

    def __del__(self):
        del self.surname
        del self.position
        del self.salary

    def increaseSalaryOn15Perc(self):
        self.salary = math.ceil(self.salary * 1.15)

    def ivanParty(self):
        if self.surname.startswith("Ivan"):
            self.position = "engineer"


# task 2
d = [Employee_Task11("Biba", "manager", 25000)]

for i in d:
    print(i)
    i.increaseSalaryOn15Perc()
    i.ivanParty()
    print(i)
    print()
