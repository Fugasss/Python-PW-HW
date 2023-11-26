from Date import Date


class Employee_Task8:
    def __init__(self, surname, salary, birthdate: Date):
        self.surname = surname
        self.salary = salary
        self.birthdate = birthdate

    def __str__(self):
        return f'{self.surname} {self.salary} {self.experience}'

    def __del__(self):
        del self.surname
        del self.salary
        del self.experience

        print(Employee_Task8.__name__, 'deleted')

    def calculateAge(self):
        dy = 2023 - self.birthdate.year
        dm = 11 - self.birthdate.month
        dd = 26 - self.birthdate.day

        if dm < 0:
            dy += 1
        elif dm == 0 and dd <= 0:
            dy += 1

        print(f"{self.surname}'s age is {dy}")
        return dy

    def daysBefore50(self):
        age = self.calculateAge()

        if age >= 50:
            print(f"{self.surname} is already 50 years old")
            return

        current_date = Date(26, 11, 2023)
        final_date = Date(self.birthdate.day, self.birthdate.month, self.birthdate.year + 50)




# task 2
d = [Employee_Task8("Biba", 25000, 4),
     Employee_Task8("Boba", 390000, 12),
     Employee_Task8("JoJa", 5000, 1)]

for i in d:
    print(i)
    i.calculateAge()
    i.daysBefore50()
    print(i)
    print()
