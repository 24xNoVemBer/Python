import math

def solve():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                j = n // i
                if i % 2 == 0:
                    count += 1
                if j % 2 == 0 and j != i:
                    count += 1
        print(count)
solve()