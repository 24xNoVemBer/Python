test_cases = int(input())
arr = []
for cases in range(test_cases):
    s = input().strip()
    while s[0] == ' ':
        s = s[1:]
    while s[len(s)-1] == ' ':
        s = s[0:len(s)-1]
    if arr.count(s) == 0:
        arr.append(s)
print(len(arr))