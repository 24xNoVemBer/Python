import sys, math
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 40

def fmt(x: Decimal) -> str:
    if (x == x.to_integral_value()):
        return f"{int(x)}.0"

    s0 = format(x.normalize(), 'f').rstrip('0').rstrip('.')
    if '.' in s0:
        frac0 = s0.split('.')[1]
        if len(frac0) < 5:
            return s0

    d5 = x.quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)
    s5 = format(d5, 'f').rstrip('0').rstrip('.')

    if '.' in s5 and len(s5.split('.')[1]) == 5:
        d4 = x.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        s4 = format(d4, 'f').rstrip('0').rstrip('.')
        return s4 if '.' in s4 else s4 + '.0'

    return s5 if '.' in s5 else s5 + '.0'

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        b, ls = map(Decimal, sys.stdin.readline().split())
        rs_min = (ls*ls - b*b).sqrt()
        rs_max = (ls*ls + b*b).sqrt()
        print(f"{fmt(rs_min)} {fmt(rs_max)}")

if __name__ == "__main__":
    solve()
