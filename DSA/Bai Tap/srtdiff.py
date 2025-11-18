def solve(S1:list,S2:list) -> list:
    arr =[]
    for i in S1:
        if i not in S2 and i not in arr:
            arr.append(i)
    arr.sort()
    return arr
def main():
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = input().split()
        s2 = input().split()
        a = solve(s1,s2)
        print(*a)
main()
