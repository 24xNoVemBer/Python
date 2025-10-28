class Rectangle:
    def __init__(self, width, height,color):
        self.width = width
        self.height = height
        self.color = color
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def p_color(self):
        return self.color.capitalize()
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = arr[2]
ps = Rectangle(a, b, c)
if a > 0 and b > 0:
    print(ps.perimeter(),ps.area(), ps.p_color())
else:
    print("INVALID")
