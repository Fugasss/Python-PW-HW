# 1
class Employee:
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

        print(Employee.__name__, 'deleted')

    def func1(self):
        print(self.experience)

    def func2(self):
        print(self.experience)


d = [Employee("Biba", 25000, 4), Employee("Boba", 390000, 12), Employee("JoJa", 5000, 1)]

for i in d:
    print(i)
    i.func1()
    i.func2()
    print(i)
    print()
