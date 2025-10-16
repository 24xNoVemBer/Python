# Nhập code của bạn ở đây
def solve():
    test_case = int(input())
    for test in range(test_case):
        number = int(input())
        s = input().strip()
        print(len(s) - max(s.count('R'), s.count('G'), s.count('B')))
    pass

if __name__ == "__main__":
    solve()
