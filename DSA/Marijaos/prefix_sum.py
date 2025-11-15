def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if n == 0:
        for _ in range(k):
            print(0)
        return

    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    for _ in range(k):
        l, r = map(int, input().split())
        print(prefix_sum[r - 1] - (prefix_sum[l - 2] if l > 1 else 0))

solve()

