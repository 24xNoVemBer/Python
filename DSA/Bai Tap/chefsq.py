# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        l1 = int(input())
        s = list(map(int, input().split()))
        l2 = int(input())
        s1 = list(map(int, input().split()))
        kt = False
        for i in range(l1 - l2 + 1):
            if s[i:i + l2] == s1:
                kt = True
                break
        if kt:
            print("Yes")
        else:
            print("No")
    pass

if __name__ == "__main__":
    solve()
