import math

N = 10**6 + 5
is_prime = [True] * N
is_prime[0] = is_prime[1] = False

p = 2
while p * p < N:
    if is_prime[p]:
        for x in range(p * p, N, p):
            is_prime[x] = False
    p += 1
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        num = int(input())
        count = 0
        for i in range(num):
            if math.gcd(i,num) == 1:
                count += 1
        if is_prime[count]:
            print("YES")
        else:
            print("NO")
solve()