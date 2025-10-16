# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        s = input().strip()
        print(len(s) - s.count('4') - s.count('7'))
    pass

if __name__ == "__main__":
    solve()
