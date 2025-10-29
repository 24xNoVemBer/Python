import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

class fraction_class:
    def __init__(self, ts , ms):
        self.ts = ts
        self.ms = ms
    def shorten(self,other):
        tsc = (self.ts * lcm(self.ms, other.ms)// self.ms) + (other.ts * lcm(self.ms, other.ms)// other.ms)
        msc = lcm(self.ms, other.ms)
        return str(tsc // math.gcd(tsc,msc)) + '/' + str(msc // math.gcd(tsc,msc))
arr = list(map(int, input().split()))
s1 = fraction_class(arr[0], arr[1])
s2 = fraction_class(arr[2], arr[3])
print(s1.shorten(s2))