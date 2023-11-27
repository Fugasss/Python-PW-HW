import math


class Rect:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def inpix(self):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)

        print(f"{dx}x{dy} pixels")

    def diag(self):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2

        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

        print(f"Diagonal = {d:.2f}")


rects = [
    Rect(12, 32, 512, 640),
    Rect(0, 32, 333, 320),
    Rect(5, 3, 384, 215),
]

for i in rects:
    i.inpix()
    i.diag()