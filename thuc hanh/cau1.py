test_cases = int(input())
for i in range(test_cases):
    a , b = map(int, input().split())
    print((a+b)*2,end=' ')
    print(a*b)