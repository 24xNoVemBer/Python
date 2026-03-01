testcase = int(input())
for _ in range(testcase):
    n = int(input())
    lcm = 1
    for i in range(2, n + 1):
        a, b = lcm, i
        while b:
            a, b = b, a % b
        gcd = a
        lcm = lcm * i // gcd
    print(lcm)