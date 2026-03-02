test_case = int(input())
a = []
for t in range(test_case):
    s = input().strip()
    a.append(s)
print(len(set(a)))