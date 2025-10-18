# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n , m = map(int, input().split())
        if (n >= 2 and m >= 2) and (n*m %2==0):
            print("Yes")
        else:
            print("No")
    pass

if __name__ == "__main__":
    solve()
