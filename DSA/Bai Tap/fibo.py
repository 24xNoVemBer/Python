arr_fibo = [0, 1]
while True:
    nxt = arr_fibo[-1] + arr_fibo[-2]
    if nxt > 10**18:
        break
    arr_fibo.append(nxt)

set_fibo = set(arr_fibo)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 0:
            print("NO")
        else:
            print("YES" if n in set_fibo else "NO")
solve()
