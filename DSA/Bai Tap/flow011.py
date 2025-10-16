# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        salary = int(input())
        if salary < 1500:
            k = salary + salary*0.1 + salary*0.9
        else:
            k = salary + 500 + salary*0.98
        if abs(k - round(k)) < 1e-9:
            print(str(int(round(k))))
        else:
            print(f"{k:.1f}")
    pass

if __name__ == "__main__":
    solve()
