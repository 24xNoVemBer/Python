# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        st = []
        for i in range(n):
            s = input()
            st.append(s)
        st = st[::-1]
        k = [s.split() for s in st]
        for i in range(n):
            if i == 0:
                print("Begin",end=' ')
                print(*k[i][1:])
            else:
                if k[i-1][0] == "Left":
                    print("Right",end=' ')
                    print(*k[i][1:])
                else:
                    print("Left",end=' ')
                    print(*k[i][1:])
    pass

if __name__ == "__main__":
    solve()