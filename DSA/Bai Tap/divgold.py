
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        b = s
        a = list(s)
        for i in range(n):
            ch = a[i]
            res = a[:i] + a[i+1:]
            for j in range(n):
                c = ''.join(res[:j] + [ch] + res[j:])
                if c < b:
                    b = c
        print(b)

if __name__ == "__main__":
    solve()