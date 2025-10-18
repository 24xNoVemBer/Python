# Nhập code của bạn ở đây
def solve():
    number_city = int(input())
    name_city = input().split()
    prices_city = int(input())
    menu = {}
    for _ in range(prices_city):
        prices = input().split()
        key = prices[0] + ' ' + prices[1]
        value = int(prices[2])
        menu[key] = value
    test_case = int(input())
    for _ in range(test_case):
        s = input().split()
        res = 0
        if s[0] == '1':
            if s[1] in name_city:
                print('0')
            else:
                print('ERROR')
        else:
            kt = True
            for i in range(1,len(s)-1):
                distance = s[i] + ' '+ s[i+1]
                if s.count(s[i]) > 1:
                    print('ERROR')
                    kt = False
                    break
                else:
                    if menu.get(distance) is not None:
                       res += menu[distance]
                    else:
                        print("ERROR")
                        kt = False
                        break
            if kt:
                print(res)
    pass

if __name__ == "__main__":
    solve()
