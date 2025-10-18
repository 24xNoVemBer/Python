MOD = 10**9 + 7

def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        print((pow(2, n, MOD) - 1) % MOD)

if __name__ == "__main__":
    solve()
