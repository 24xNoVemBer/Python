# Nhập code của bạn ở đây
def solve():
    test_case = int(input())
    for case in range(test_case):
        s = input()
        max_s = 0
        s1 = ""
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
               s1 += s[i]
            else:
                if s1!="":
                    max_s = max(max_s,int(s1))
                    s1 = ""
            if s1!="":
                max_s = max(max_s,int(s1))
        print(max_s)
    pass

if __name__ == "__main__":
    solve()
