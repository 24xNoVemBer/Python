test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    s = input().strip()
    arr = s.split()
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) + 1
    for key, value in count.items():
        print(key, value)