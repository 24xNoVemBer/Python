test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    a = set(map(int, input().split()))
    print(len(a))