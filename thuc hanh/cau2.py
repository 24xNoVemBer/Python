test_cases = int(input())
for t in range(test_cases):
    a , b ,c = map(int, input().split())
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('YES')
    else:
        print('NO')
