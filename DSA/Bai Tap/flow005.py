def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        cost = [100, 50, 10, 5, 2, 1]
        count = 0
        for c in cost:
            count += n // c
            n %= c
        print(count)


pass

if __name__ == "__main__":
    solve()
