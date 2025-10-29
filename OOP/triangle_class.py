import math
import sys

class point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

class triangle():
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def chu_vi(self):
        return self.a + self.b + self.c

    def check(self):
        a, b, c = self.a, self.b, self.c
        return (a + b > c ) and (a + c > b ) and (b + c > a )


data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1
for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, data[idx:idx + 6])
    idx += 6
    p1 = point(x1, y1)
    p2 = point(x2, y2)
    p3 = point(x3, y3)

    c1 = p1.distance(p2)
    c2 = p1.distance(p3)
    c3 = p2.distance(p3)

    cv = triangle(c1, c2, c3)
    if cv.check():
        print(f"{cv.chu_vi():.3f}")
    else:
        print("INVALID")
