def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    cur_sum =0
    max_sum = 0

    for i in arr:
        cur_sum = max(i, cur_sum + i)
        cur_sum = max(cur_sum, 0)
        max_sum = max(max_sum, cur_sum)
    print(max_sum)

solve()