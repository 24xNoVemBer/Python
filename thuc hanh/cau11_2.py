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
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    nt_max = None
    for i in arr:
        if is_prime[i]:
            if nt_max == None:
                nt_max = i
            else:
                nt_max = max(nt_max, i)
    print(nt_max)
