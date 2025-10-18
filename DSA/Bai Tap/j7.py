import math

def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        p , s = map(float, input().split())
        x = (p - math.sqrt(p * p - 24 * s)) / 12
        v = x * x * ((p / 4) - 2 * x)
        print(f"{v:.2f}")

if __name__ == "__main__":
    solve()
