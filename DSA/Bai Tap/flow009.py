# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n , k = map(int, input().split())
        if n <= 1000:
            print(f"{n*k:.6f}")
        else:
            print(f"{n*0.9*k:.6f}")
    pass

if __name__ == "__main__":
    solve()
