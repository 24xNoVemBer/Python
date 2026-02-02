N, K = map(int, input().split())

a = [0] * K
count = 0

def backtrack(n, k):
    global count
    if n == K:
        print("".join(map(str, a)), end=" ")
        count += 1
        return

    for i in range(k, N + 1):
        a[n] = i
        backtrack(n + 1, i + 1)

backtrack(0, 1)
print()
print(f"Tong cong co {count} to hop")
