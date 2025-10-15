# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        l , region = input().split()
        num = int(l)
        count = 0
        for i in range(num):
            arr = input().split()
            s = arr[0]
            if s == "CONTEST_WON":
                count += 300 + max(20 - int(arr[1]),0)
            if s == "TOP_CONTRIBUTOR":
                count += 300
            if s == "BUG_FOUND":
                count += int(arr[1])
            if s == "CONTEST_HOSTED":
                count += 50
        if region == "INDIAN":
            print(count//200)
        else:
            print(count//400)
    pass

if __name__ == "__main__":
    solve()
