def solve():
    a, b = map(int, input().split())
    s = list(str(a - b))
    if s[0] != '1':
        s[0] = '1'
    else:
        s[0] = '2'
    print(''.join(s))

if __name__ == "__main__":
    solve()
