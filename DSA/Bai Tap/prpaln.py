def check(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
        l += 1
        r -= 1
    return True

def solve():
    test_cases = int(input())
    for case in range(test_cases):
        s = input().strip()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    solve()
