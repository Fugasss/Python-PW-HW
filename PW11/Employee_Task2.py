# 1
class Employee_Task2:
    def __init__(self, surname, salary, experience):
        self.surname = surname
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return f'{self.surname} {self.salary} {self.experience}'

    def __del__(self):
        del self.surname
        del self.salary
        del self.experience

        print(Employee_Task2.__name__, 'deleted')

    def func1(self):
        print(self.experience)

    def func2(self):
        print(self.experience)


# task 2
d = [Employee_Task2("Biba", 25000, 4), Employee_Task2("Boba", 390000, 12), Employee_Task2("JoJa", 5000, 1)]

for i in d:
    print(i)
    i.func1()
    i.func2()
    print(i)
    print()

