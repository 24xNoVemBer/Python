# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        count = 0
        while n>=5 :
            n//=5
            count += n
        print(count)
    pass

if __name__ == "__main__":
    solve()
