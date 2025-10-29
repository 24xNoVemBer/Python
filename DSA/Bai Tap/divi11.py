def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        if n % 11 == 0:
            print(1)
        else:
            print(0)
solve()