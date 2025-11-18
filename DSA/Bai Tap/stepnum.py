def check(s:str) -> bool:
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) != 1:
            return False
    return True
def main():
    test_cases = int(input())
    for _ in range(test_cases):
        S = input().strip()
        if check(S):
            print("YES")
        else:
            print("NO")
main()