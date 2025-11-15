def solve():
    s = input()
    count_0 = 0
    count_1 = 0
    res = []
    res.append(0)
    for i in s:
        if i == '0':
            count_0 += 1
        if i == '1':
            count_1 += 1
        if count_0 == count_1:
            res[len(res)-1] += 1
            res.append(res[len(res)-1]+res[len(res)-2])
    print(res[len(res)-1])
solve()