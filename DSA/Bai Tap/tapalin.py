# Nhập code của bạn ở đây
def solve():
    MOD = 10**9 + 7
    inv25 = pow(25, MOD - 2, MOD)
    def count(N):
        if N <= 0:
            return 0
        m = N // 2
        if m == 0:
            S = 0
        else:
            S = (26 * (pow(26, m, MOD) - 1)) % MOD
            S = (S * inv25) % MOD
        if N % 2 == 0:
            return (2 * S) % MOD
        else:
            return (2 * S + pow(26, m + 1, MOD)) % MOD

    test_cases = int(input().strip())
    for _ in range(test_cases):
        n = int(input().strip())
        print(count(n))

if __name__ == "__main__":
    solve()
