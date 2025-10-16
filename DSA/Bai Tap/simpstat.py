# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        a = a[k:n-k]
        print(f"{sum(a)/len(a):.6f}")
    pass

if __name__ == "__main__":
    solve()
