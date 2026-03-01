def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        number = int(input())
        kt = True
        if is_prime(number) == False:
            kt = False
        else:
            rv = str(number)
            rv = rv[::-1]
            k = int(rv)
            if is_prime(k) == False:
                kt = False
            else:
                s = str(number)
                tong = sum(int(digit) for digit in s)
                if is_prime(tong) == False:
                    kt = False
                else:
                    for i in s:
                        if is_prime(int(i)) == False:
                            kt = False
        if kt:
            print("Yes")
        else:
            print("No")
solve()