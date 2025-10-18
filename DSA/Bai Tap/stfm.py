import math as m
def solve():
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in arr:
        res += (m.factorial(i+1) - 1 + (i**2*(i+1))//2) % k
        res %=k
    print(res)
    pass

if __name__ == "__main__":
    solve()
