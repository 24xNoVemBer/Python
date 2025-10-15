# Nhập code của bạn ở đây
def solve():
    def kt(s):
        balance = 0
        max_balance =0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            if s[i] == ')':
                balance -= 1
            max_balance = max(max_balance, balance)
        return max_balance
    test_case = int(input())
    for test in range(test_case):
        st = input()
        k = kt(st)
        for i in range(k):
            print('(',end='')
        for i in range(k):
            print(')', end='')
    pass

if __name__ == "__main__":
    solve()
