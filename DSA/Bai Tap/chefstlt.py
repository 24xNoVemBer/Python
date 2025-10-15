# Nhập code của bạn ở đây
def solve():
    test_case = int(input())
    for _ in range(test_case):
        s1 = input().strip()
        s2 = input().strip()
        max_s = 0
        min_s = 0
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if s1[i] == s2[i] == '?':
                max_s +=1
            if (s1[i] != s2[i]) and (s1[i] != '?') and (s2[i] != '?'):
                min_s += 1
        print(min_s,max_s +count)


    pass

if __name__ == "__main__":
    solve()
