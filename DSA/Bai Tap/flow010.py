# Nhập code của bạn ở đây
def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        char_x = input().strip()
        if char_x == 'B' or char_x == 'b':
            print("BattleShip")
        if char_x == 'C' or char_x == 'c':
            print("Cruiser")
        if char_x == 'D' or char_x == 'd':
            print("Destroyer")
        if char_x == 'F' or char_x == 'f':
            print("Frigate")
    pass

if __name__ == "__main__":
    solve()
