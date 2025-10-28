def check(k):
    s = str(k)
    if len(s) == 1:
        return True
    else:
        if s == s[::-1]:
            return True

def solve():
    test_case = int(input())
    for case in range(test_case):
        a,b = map(int, input().split())
        count = 0
        for i in range(a,b+1):
            if check(i):
                count+=i
        print(count)
    pass
if __name__ == "__main__":
    solve()
