# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        count_a = []
        count_a.append(1)
        for i in range(1,n):
            if a[i] >= a[i-1]:
                count_a.append(count_a[i-1] + 1)
            else:
                count_a.append(1)
        print(sum(count_a))
    pass

if __name__ == "__main__":
    solve()
