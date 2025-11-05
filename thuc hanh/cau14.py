def tcs(N):
    res = 0
    s = str(N)
    for i in s:
        res += int(i)
    return res
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    for j in arr:
        print(tcs(j),end=' ')
    print()