
N = 10**6 + 5
is_prime = [True] * N
is_prime[0] = is_prime[1] = False

p = 2
while p * p < N:
    if is_prime[p]:
        for x in range(p * p, N, p):
            is_prime[x] = False
    p += 1

primes = [i for i in range(2, N) if is_prime[i]]

def is_palindrome_num(k: int) -> bool:
    s = str(k)
    return s == s[::-1]

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        out = []
        for k in primes:
            if k >= n:
                break
            if is_palindrome_num(k):
                continue
            r = int(str(k)[::-1])
            if r > k and r < N and is_prime[r]:
                out.append(f"{k} {r}")
        print("  ".join(out))

solve()
