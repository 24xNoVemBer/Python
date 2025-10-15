# Nhập code của bạn ở đây
def solve():
    prices = []
    for i in range(12):
        prices.append(2**i)
    test_cases = int(input())
    for _ in range(test_cases):
        num = int(input())
        count = 0
        while num > 0:
            for i in range(11,-1,-1):
                if num >= prices[i]:
                    num -= prices[i]
                    count += 1
                    break
        print(count)
    pass

if __name__ == "__main__":
    solve()
