def check(N:int) -> list:
    arr = []
    if N % 2 == 0:
        count = 0
        while N % 2 == 0:
            count += 1
            N //= 2
        arr.append((2, count))
    i = 3
    while i * i <= N:
        if N % i == 0:
            count = 0
            while N % i == 0:
                count += 1
                N //= i
            arr.append((i, count))
        i += 2
    if N > 1:
        arr.append((N, 1))
    return arr
def main():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        res = check(n)
        print(f"Test {_+1}: ",end='')
        for p , e in res:
            print(f"{p}({e})",end=' ')
        print()
main()