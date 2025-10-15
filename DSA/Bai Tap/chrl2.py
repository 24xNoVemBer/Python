# Nhập code của bạn ở đây
def solve():
    s = input().strip()
    need = "CHEF"
    j = 0
    count = 0
    for i in s:
        if i == need[j]:
            j += 1
            if j == 4:
                count += 1
                j = 0
    print(count)
    pass

if __name__ == "__main__":
    solve()
