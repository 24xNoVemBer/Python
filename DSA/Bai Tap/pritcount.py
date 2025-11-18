N = 10**6 + 5
is_prime = [True] * N
is_prime[0] = is_prime[1] = False

p = 2
while p * p < N:
    if is_prime[p]:
        for x in range(p * p, N, p):
            is_prime[x] = False
    p += 1
prime = []
for i in range(N):
    if is_prime[i]:
        prime.append(i)
def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        count = 0
        for i in range(n):
            if prime[i] +6 <=n:
                if (is_prime[prime[i]+2] and is_prime[prime[i]+6]) or (is_prime[prime[i]+4] and is_prime[prime[i]+6]):
                    count+=1
            else:
                break
        print(count)
main()