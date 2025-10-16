# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        nguyen_lieu = list(map(int, input().split()))
        if 1 in nguyen_lieu:
            print(-1)
        else:
            print(sum(nguyen_lieu) - max(nguyen_lieu) +2 )
    pass

if __name__ == "__main__":
    solve()
