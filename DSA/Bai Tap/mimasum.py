n , s = map(int, input().split())
S = s
if n*9 < s:
    print(-1,-1)
else:
    if s == 0:
        if n == 1:
            print(0, 0)
        else:
            print(-1, -1)
    else:
        s1=''
        s2=''
        d=1
        k=9
        while n>0:
            while d<=9:
                if s - d <= (n - 1) * 9:
                    s -= d
                    s1 += str(d)
                    break
                d += 1
            while k>=0:
                if S - k >= 0 and S - k <= (n - 1) * 9:
                    S -= k
                    s2 += str(k)
                    break
                k -= 1
            d=0
            k=9
            n-=1
        print(s1,s2)
