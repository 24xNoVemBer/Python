N = 10**6 + 5
is_prime = [True] * N
is_prime[0] = is_prime[1] = False

p = 2
while p * p < N:
    if is_prime[p]:
        for x in range(p * p, N, p):
            is_prime[x] = False
    p += 1
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    max_s = 0
    for j in arr:
        if is_prime[j]:
            max_s = max(max_s, j)
    print(max_s)