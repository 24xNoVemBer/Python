def interchange_sort_minimal(a):
    n = len(a)
    buoc = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

        buoc += 1
        print(f"Buoc {buoc}: {' '.join(map(str, a))}")

    return a


n = int(input())
a = list(map(int, input().split()))
interchange_sort_minimal(a)