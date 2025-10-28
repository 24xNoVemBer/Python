# Nhập code của bạn ở đây
import math

def solve():
    a, b, c = map(float, input().split())
    if a == 0:
        if b == 0:
            if c == 0:
                print("VSN")
            else:
                print("VN")
        else:
            x = -c / b
            print(f"{x:.6f}")
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("VN")
        elif delta == 0:
            x = -b / (2*a)
            print(f"{x:.6f}")
        else:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            if x1 > x2:
                x1, x2 = x2, x1
            print(f"{x1:.6f} {x2:.6f}")

if __name__ == "__main__":
    solve()
