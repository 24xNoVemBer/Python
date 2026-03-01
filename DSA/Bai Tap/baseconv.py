def base_4(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 4))
        n //= 4
    return ''.join(digits[::-1])

test_cases = int(input())
for _ in range(test_cases):
    b = int(input())
    s = input().strip()
    n = int(s, 2)

    if b == 2:
        print(s)
    elif b == 4:
        print(base_4(n))
    elif b == 8:
        print(oct(n)[2:])
    elif b == 16:
        print(hex(n)[2:].upper())
