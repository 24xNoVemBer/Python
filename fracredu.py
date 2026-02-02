import math
a,b = map(int, input().split())
print(f"{a // math.gcd(a,b)}/{b // math.gcd(a,b)}")