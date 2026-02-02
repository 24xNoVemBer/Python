s = input().strip()
n = len(s)
i = 0
ans = 0

while i < n:
    if s[i] == 'B':
        start = i
        length = 0
        while i < n and s[i] == 'B':
            length += 1
            i += 1

        if length == 1:
            ans += 1
        else:
            if start == 0:
                ans += 1
            else:
                ans += 2
    else:
        i += 1

print(ans)
