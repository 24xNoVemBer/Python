# Nhập code của bạn ở đây

import math as m

def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int, input().split())
        print(m.gcd(a,b))
    pass

if __name__ == "__main__":
    solve()
