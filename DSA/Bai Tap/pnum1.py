def check(s:str) -> bool:
    if s != s[::-1]:
        return False
    if s[0] != '8' or s[len(s) - 1] != '8':
        return False
    res = 0
    for i in range(len(s)):
        res += int(s[i])
    if res%10!=0:
        return False
    return True
def main():
    test_cases = int(input())
    for _ in range(test_cases):
        k = input().strip()
        if check(k):
            print("YES")
        else:
            print("NO")
main()