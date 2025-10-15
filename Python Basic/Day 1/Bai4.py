a, b, c = list(map(int, input().split()))

p = (a+b+c)/2

print((p*(p-a)*(p-b)*(p-c))**0.5)