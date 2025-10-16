# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        number = int(input())
        dp = [list(map(int, input().split())) for _ in range(number)]
        for i in range(number-2,-1,-1):
            for j in range(i+1):
                dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
        print(dp[0][0])
    pass


if __name__ == "__main__":
    solve()
