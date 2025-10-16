# Nhập code của bạn ở đây
def solve():
    test_case = int(input())
    for i in range(test_case):
        a,b,c = map(int,input().split())
        if (a+b+c ==180) and (a>0) and (b>0) and (c>0):
            print("YES")
        else:
            print("NO")
    pass

if __name__ == "__main__":
    solve()
