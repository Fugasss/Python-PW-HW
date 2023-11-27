class Book_Task3:
    def __init__(self, title: str, pages: int, price: float):
        self.title = title
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title}, {self.pages} pages, {self.price} tg"

    def increasepagescount(self, p):
        self.pages += p

    def decreaseprice2t(self):
        if self.pages > 100:
            self.price //= 2



books_t12 = [
    Book_Task3("Programming booba", 123, 5050),
    Book_Task3("Small boobs good too", 3, 500),
    Book_Task3("Yes, ma masta'", 999, 50000),
]

for i in books_t12:
    print(i)
    i.increasepagescount(10)
    i.decreaseprice2t()
    print(i)
    print()
