# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        str_x = input()
        str_y = input()
        str_z = ""
        for i in range (len(str_x)):
            if str_y[i] == str_x[i]:
                if str_y[i] == 'W':
                    str_z+='B'
                else:
                    str_z+='W'
            else:
                str_z+='B'
        print(str_z)
    pass

if __name__ == "__main__":
    solve()
