def is_palindrome_num(k: int) -> bool:
    s = str(k)
    return s == s[::-1]
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in arr:
        if is_palindrome_num(i):
            count += 1
    print(count)