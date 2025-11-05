test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    k = min(arr)
    if k  < 0:
        print(k)
    else:
        print(0)