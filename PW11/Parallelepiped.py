class Parallelepiped:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        v = self.a * self.b * self.c
        print(f"Volume = {v}")

    def squaresurfacesarea(self):
        s = 0
        a = self.a
        b = self.b
        c = self.c

        s += 2 * a * b if a == b else 0
        s += 2 * a * c if a == c else 0
        s += 2 * b * c if b == c else 0

        print(f"Area of square surfaces = {s}")


prs = [
    Parallelepiped(2, 3, 4),
    Parallelepiped(4, 5, 2),
    Parallelepiped(3, 3, 3),
    Parallelepiped(5, 7, 2)
]

for i in prs:
    i.squaresurfacesarea()
    i.volume()
    print()
