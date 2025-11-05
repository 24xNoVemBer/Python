def check_nt(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    if check_nt(n):
        print("YES")
    else:
        print("NO")