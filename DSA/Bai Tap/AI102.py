n, q = map(int, input().split())
a = list(map(int, input().split()))

A = [0]*n
A[0] = a[0]

for i in range(1, n):
    A[i] = A[i-1] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    if l == 1:
        print(A[r-1])
    else:
        print(A[r-1] - A[l-2])