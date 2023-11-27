import math


class Product_Task14:
    def __init__(self, name: str, price: float, manufacturer: str):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer

    def __str__(self):
        return f"{self.name}, {self.manufacturer}, {self.price}"

    def priceineuro(self):
        print(f"The price of product in euro is {self.price / 502}")

    def SamsungParty(self):
        if self.manufacturer.find("Samsung") != -1:
            self.price = math.ceil(self.price / 502 * 2) * 499


products_t14 = [
    Product_Task14("Phone", 2500, "Samsung"),
    Product_Task14("Dickenson", 66669999, "Chingug"),
    Product_Task14("(′д｀σ)σ～(　TロT)σ(ノ｀Д)ノ(〃＞目＜)", 696969, "Huiwei"),
]

for i in products_t14:
    print(i)
    i.priceineuro()
    i.SamsungParty()
    print(i)
    print()
