MAX_N = 10000000
is_prime_sieve = [True] * (MAX_N + 1)
is_prime_sieve[0] = is_prime_sieve[1] = False

# Sieve computation
for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime_sieve[i]:
        for j in range(i*i, MAX_N + 1, i):
            is_prime_sieve[j] = False

num = int(input())
for _ in range(num):
    a = int(input())
    if a <= MAX_N:
        if is_prime_sieve[a]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")