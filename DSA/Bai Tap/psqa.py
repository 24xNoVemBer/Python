import math
def check(N:int) -> bool:
    if round(math.sqrt(N))**2 == N:
        return True
    return False
def main():
    n = int(input())
    for i in range(n):
        k = int(input())
        if check(k):
            print("YES")
        else:
            print("NO")
main()