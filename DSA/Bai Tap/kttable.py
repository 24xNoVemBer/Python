# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        student = list(map(int, input().split()))
        time = list(map(int, input().split()))
        count = 0
        if time[0] <= student[0]:
            count += 1
        for i in range(1,n):
            if time[i] <= (student[i]-student[i-1]):
                count += 1
        print(count)
    pass

if __name__ == "__main__":
    solve()
