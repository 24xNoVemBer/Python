import math

def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        arr = list(map(float, input().split()))
        goc = arr[0]
        lai = arr[1]/100
        tien = arr[2]
        print(math.ceil(math.log(tien / goc) / math.log(1 + lai)))
solve()