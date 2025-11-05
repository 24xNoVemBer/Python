import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


test_cases = int(input())
for _ in range(test_cases):
    a , b = map(int, input().split())
    print(math.gcd(a, b),lcm(a,b))