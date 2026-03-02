N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

B = [list(map(int, input().split())) for _ in range(K)]

rows = N - K + 1
cols = M - K + 1

C = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        total = 0
        for u in range(K):
            for v in range(K):
                total += A[i+u][j+v] * B[u][v]
        C[i][j] = total

for row in C:
    print(*row)