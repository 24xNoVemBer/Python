import math

def gcd_list(lst):
    g = lst[0]
    for x in lst[1:]:
        g = math.gcd(g, x)
    return g

def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().split()))
        a = a[1:]
        g = gcd_list(a)
        for i in range(len(a)):
            print(a[i] // g, end=' ')
        print()
    pass

if __name__ == "__main__":
    solve()
