# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        s = input().strip()
        d1 , d2 =0,0
        for i in range(len(s)):
            if i%2==0:
                if s[i] == '-':
                    d1 += 1
                else:
                    d2 += 1
            else:
                if s[i] == '-':
                    d2+=1
                else:
                    d1 += 1
        print(len(s)-max(d1,d2))
    pass

if __name__ == "__main__":
    solve()
