# Nhập code của bạn ở đây
def solve():
    number = int(input())
    a = []
    for _ in range(number):
        k = int(input())
        a.append(k)
    a.sort()
    for _ in a:
        print(_)
    pass
if __name__ == "__main__":
    solve()
