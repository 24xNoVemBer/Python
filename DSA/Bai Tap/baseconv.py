test_cases = int(input())
for _ in range(test_cases):
    b = int(input())
    s = input().strip()
    n = int(s, 2)

    if b == 2:
        print(s)
    elif b == 4:
        print(format(n, 'o').replace('8','10'))
    elif b == 8:
        print(oct(n)[2:])
    elif b == 16:
        print(hex(n)[2:].upper())
