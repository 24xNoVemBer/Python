# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        a = input().strip()
        b = input().strip()
        kt = False
        for i in a:
            if i in b:
                print("Yes")
                kt =True
                break
        if not kt:
            print("No")

    pass

if __name__ == "__main__":
    solve()
