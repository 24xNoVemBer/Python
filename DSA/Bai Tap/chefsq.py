# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        l1 = int(input())
        s = input().strip()
        l2 = int(input())
        s1 = input().strip()
        if s1 in s:
            print("Yes")
        else:
            print("No")
    pass

if __name__ == "__main__":
    solve()
