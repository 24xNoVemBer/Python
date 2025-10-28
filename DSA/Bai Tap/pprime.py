N = 10**7 + 5

is_prime = [True] * N

is_prime[0] = False
is_prime[1] = False
p = 2
while p * p <= N:
    if is_prime[p]:
        for i in range(p * p, N, p):
            is_prime[i] = False
    p+=1
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        number = int(input())
        kt = True
        if is_prime[number] == False:
            kt = False
        else:
            rv = str(number)
            rv = rv[::-1]
            k = int(rv)
            if is_prime[k] == False:
                kt = False
            else:
                s = str(number)
                tong = sum(int(digit) for digit in s)
                if is_prime[tong] == False:
                    kt = False
                else:
                    for i in s:
                        if is_prime[int(i)] == False:
                            kt = False
        if kt:
            print("YES")
        else:
            print("NO")
solve()

