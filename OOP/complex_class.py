import builtins as B

class complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pt_c(self, other):
        z1 = B.complex(self.a, self.b)
        z2 = B.complex(other.a, other.b)
        return (z1 + z2) * z1

    def pt_d(self, other):
        z1 = B.complex(self.a, self.b)
        z2 = B.complex(other.a, other.b)
        return (z1 + z2) ** 2
def fmt(z):
    A, B = int(z.real), int(z.imag)
    sign = '+' if B >= 0 else '-'
    return f"{A} {sign} {abs(B)}i"
def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        a, b, c, d = map(int, input().split())
        cp_1 = complex(a, b)
        cp_2 = complex(c, d)
        r1 = cp_1.pt_c(cp_2)
        r2 = cp_1.pt_d(cp_2)
        print(f"{fmt(r1)}, {fmt(r2)}")

solve()
