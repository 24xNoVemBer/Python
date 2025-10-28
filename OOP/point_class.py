import math

class point():
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def distance(self,other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
test_case = int(input())
for i in range(test_case):
    arr = list(map(float, input().split()))
    p1 = point(arr[0],arr[1])
    p2 = point(arr[2],arr[3])
    print(f"{p1.distance(p2):.4f}")