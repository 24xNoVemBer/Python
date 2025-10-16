# Nhập code của bạn ở đây
def solve():
    test_case = int(input())
    for case in range(test_case):
        n = int(input())
        arr = list(map(int, input().split()))
        l = max(arr)
        last_index = len(arr) - 1 - arr[::-1].index(l)
        print(l + last_index)
    pass

if __name__ == "__main__":
    solve()
