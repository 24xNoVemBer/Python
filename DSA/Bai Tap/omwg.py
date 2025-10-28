# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n , m = map(int, input().split())
        print(2* n * m - n - m)
    pass

if __name__ == "__main__":
    solve()
