import math


class Product_Task5:
    def __init__(self, name: str, price: float, releaseyear: int):
        self.name = name
        self.price = price
        self.releaseyear = releaseyear

    def __str__(self):
        return f"{self.name}, {self.price}, {self.releaseyear}"

    def howmuchyearsbackwasreleasedproduct(self):
        dy = 2023 - self.releaseyear
        print(f"The product was released {dy} years BACK")

    def TVparty(self):
        if self.name.find("TV") != -1:
            self.price = math.ceil(self.price * 1.2)


products_t5 = [
    Product_Task5("Biba TV", 2500, 2013),
    Product_Task5("Booba Can see forever", 66669999, 1999),
    Product_Task5("Bib Bub modern robotics", 696969, 2020),
]

for i in products_t5:
    print(i)
    i.howmuchyearsbackwasreleasedproduct()
    i.TVparty()
    print(i)
    print()