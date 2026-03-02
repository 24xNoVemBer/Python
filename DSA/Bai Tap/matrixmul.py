def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
             for i in range(len(A))]

test_case = int(input())
for t in range(test_case):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    tp = transpose(matrix)
    C = multiply(matrix, tp)

    print(f"Test {t+1}:")
    for row in C:
        print(*row)


