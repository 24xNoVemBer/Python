# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(input().strip())
        b = list(input().strip())
        fa = [0]*10
        fb = [0]*10
        for x in a:
            fa[int(x)] += 1
        for x in b:
            fb[int(x)] += 1

        # Ưu tiên tạo '7'
        res7 = 0
        for i in range(8):  # ghép 7 ở A với <=7 ở B
            k = min(fa[7], fb[i])
            res7 += k
            fa[7] -= k
            fb[i] -= k
        for i in range(8):  # ghép 7 ở B với <=7 ở A
            k = min(fb[7], fa[i])
            res7 += k
            fb[7] -= k
            fa[i] -= k

        # Rồi đến '4'
        res4 = 0
        for i in range(5):  # ghép 4 ở A với <=4 ở B
            k = min(fa[4], fb[i])
            res4 += k
            fa[4] -= k
            fb[i] -= k
        for i in range(5):  # ghép 4 ở B với <=4 ở A
            k = min(fb[4], fa[i])
            res4 += k
            fb[4] -= k
            fa[i] -= k

        # In kết quả (dòng trống nếu rỗng)
        print('7'*res7 + '4'*res4)
    pass

if __name__ == "__main__":
    solve()
