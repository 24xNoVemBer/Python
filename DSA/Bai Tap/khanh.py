import math
a , b = map(int, input().split())
d = a/b
print(math.floor(d)*b)
print(math.ceil(d)*b)