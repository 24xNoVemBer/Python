# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        count = 1
        ma = a[0]
        for i in range(1,len(a)):
            if a[i] <= ma:
                ma = a[i]
                count += 1
        print(count)
    pass

if __name__ == "__main__":
    solve()
