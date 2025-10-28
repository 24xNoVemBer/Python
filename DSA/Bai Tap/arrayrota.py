test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    k  %= n
    print(*(arr[k:] + arr[:k]))
