import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

l=int(input())

for j in range(1, l+1):
    if is_prime(j) and l%j==0 :
        print(j,end=' ')
