import math

class fraction_class():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def fraction(self):
        return str(self.a//math.gcd(self.a,self.b)) + '/' + str(self.b//math.gcd(self.a,self.b))

s1,s2 = map(int, input().split())
ps = fraction_class(s1, s2)
print(ps.fraction())