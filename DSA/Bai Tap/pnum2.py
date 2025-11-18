def check(s:str) -> bool:
    if s != s[::-1]:
        return False
    for i in s:
        if i != '2' and i != '3' and i != '5' and i != '7':
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
