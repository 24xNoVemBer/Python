# Nhập code của bạn ở đây
def solve():
    t = int(input())
    for _ in range(t):
        r = int(input())
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        x3, y3 = map(int, input().split())

        r2 = r * r

        d12 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        d13 = (x1 - x3) ** 2 + (y1 - y3) ** 2
        d23 = (x2 - x3) ** 2 + (y2 - y3) ** 2

        cnt = (d12 <= r2) + (d13 <= r2) + (d23 <= r2)

        if cnt >=2:
            print("yes")
        else:
            print("no")
    pass

if __name__ == "__main__":
    solve()
a = list(map(int, input().split()))