def check(s: str) -> bool:
    if len(s) == 1:
        return True
    count = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            count += 1
    if count == 1:
        return True
    if count == 0:
        if len(s) % 2 == 1:
            return True
        else:
            return False
    return False
def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        s = input().strip()
        if check(s):
            print("YES")
        else:
            print("NO")
solve()