from datetime import datetime


class Book_Task7:
    def __init__(self, title: str, author: str, publicationdate: datetime):
        self.title = title
        self.author = author
        self.publicationdate = publicationdate

    def __str__(self):
        return f"{self.title}, {self.author}, {self.publicationdate}"

    def howmanyyears(self):
        dy = 2023 - self.publicationdate.year
        print(f"This book is {dy} years old")
        return dy

    def howmanydays(self):
        dd = datetime.today() - self.publicationdate
        print(f"This book is {dd.days} days old")
        return dd


books_t7 = [
    Book_Task7("Programming booba", "Not me", datetime(2000, 5, 22)),
    Book_Task7("Small boobs good too", "Ivan", datetime(2020, 3, 12)),
    Book_Task7("Yes, ma masta'", "Van Dark Holme", datetime(2007, 1, 23)),
]

for i in books_t7:
    print(i)
    i.howmanyyears()
    i.howmanydays()
    print(i)
    print()
