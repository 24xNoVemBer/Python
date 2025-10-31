import math, sys

EPS = 1e-9

class point:
    def __init__(self, x, y):
        self.x = float(x); self.y = float(y)
    def distance(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

class triangle:
    def __init__(self, a, b, c):
        self.a = float(a); self.b = float(b); self.c = float(c)
    def check(self):
        a, b, c = self.a, self.b, self.c
        return (a + b > c + EPS) and (a + c > b + EPS) and (b + c > a + EPS)
    def dien_tich(self):
        a, b, c = self.a, self.b, self.c
        s = (a + b + c) / 2.0
        val = s * (s - a) * (s - b) * (s - c)
        return math.sqrt(max(val, 0.0))

data = sys.stdin.read().strip().split()
t = int(data[0]); idx = 1
for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, data[idx:idx+6]); idx += 6
    p1, p2, p3 = point(x1, y1), point(x2, y2), point(x3, y3)

    a = p1.distance(p2)
    b = p1.distance(p3)
    c = p2.distance(p3)

    tri = triangle(a, b, c)
    if tri.check():
        print(f"{tri.dien_tich():.2f}")
    else:
        print("INVALID")
