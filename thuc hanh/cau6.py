test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    arr = set(map(int, input().split()))
    print(sum(arr))