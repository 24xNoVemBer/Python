# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        k = min(a)
        print(k*(n-1))
    pass

if __name__ == "__main__":
    solve()
