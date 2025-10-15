# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int,input().split())
        modern = input().split()
        data = {w: False for w in modern}
        for i in range(k):
            words = input().split()
            for w in words:
                if w in data:
                    data[w] = True
        for i in data:
            if data[i] == True:
                print("YES",end=' ')
            else:
                print("NO",end=' ')
        print('')
    pass

if __name__ == "__main__":
    solve()
