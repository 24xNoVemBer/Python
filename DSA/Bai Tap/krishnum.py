fact = [1] * 10
for i in range(1, 10):
    fact[i] = fact[i - 1] * i

testcase = int(input())
for _ in range(testcase):
    s = input().strip()
    krishnum = 0
    for char in s:
        krishnum += fact[int(char)]
    if krishnum == int(s):
        print("YES")
    else:
        print("NO")
