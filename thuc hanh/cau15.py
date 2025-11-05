test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    count = {}
    res = 0
    save = None
    for i in arr:
        count[i] = count.get(i, 0) + 1
        if count[i] >= res:
            res = count[i]
            if save == None:
                save = i
            else:
                save = min(save, i)
    print(save)