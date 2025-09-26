import math as n
a, b, c = list(map(int, input().split()))

p = (a+b+c)/2

print(n.sqrt(p*(p-a)*(p-b)*(p-c)))