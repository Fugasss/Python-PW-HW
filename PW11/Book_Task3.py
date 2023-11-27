class Book_Task3:
    def __init__(self, title: str, pages: int, price: float):
        self.title = title
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title}, {self.pages} pages, {self.price} tg"

    def avgpriceofpage(self):
        avg = self.price / self.pages
        print(f"Average price of one page: {avg}")
        return avg

    def progparty(self):
        if self.title.startswith("Programming"):
            self.price *= 2



books_t3 = [
    Book_Task3("Programming booba", 123, 5050),
    Book_Task3("Small boobs good too", 3, 500),
    Book_Task3("Yes, ma masta'", 999, 50000),
]

for i in books_t3:
    print(i)
    i.avgpriceofpage()
    i.progparty()
    print(i)
    print()