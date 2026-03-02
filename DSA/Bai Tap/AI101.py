n = int(input())
s = list(map(int, input().split()))
count = {}
for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
max_count = max(count.values())
s1 = None
for c in s:
    if count[c] == max_count:
        if s1 is None:
            s1 = c
        else:
            s1 = max(s1, c)
print(s1)
