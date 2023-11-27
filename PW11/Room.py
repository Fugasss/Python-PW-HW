class Room:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def wallsarea(self):
        l = self.l
        h = self.h
        w = self.w

        a = 2 * (l * h + w * h)

        print(f"Area of walls = {a}")

    def wallsareawithdoorandwindows(self, windowscount):
        l = self.l
        h = self.h
        w = self.w

        wa = 2 * 1.5
        da = 2 * 0.8

        a = 2 * (l * h + w * h) - da - wa * windowscount

        print(f"Area of walls without 1 door and {windowscount} windows = {a}")

rooms = [
    Room(2, 3, 4),
    Room(4, 5,2),
    Room(3, 3, 3),
    Room(5, 7, 2)
]

for i in rooms:
    i.wallsarea()
    i.wallsareawithdoorandwindows(2)
    print()
