import math

def check(a):
    if a<2:
        return False
    if a==2:
        return True
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True

test_cases = int(input())
for case in range(test_cases):
    s = input().strip()
    count = 0
    for i in s:
        if check(int(i)):
            count += 1
    if check(len(s)):
        if count > len(s) - count:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")