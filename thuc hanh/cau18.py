test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr_1 = list(map(int, input().split()))
    N = int(input())
    arr_2 = list(map(int, input().split()))
    arr_hop = []
    for i in arr_1:
        if i not in arr_hop:
            arr_hop.append(i)
    for i in arr_2:
        if i not in arr_hop:
            arr_hop.append(i)
    arr_hop.sort()
    print(*arr_hop)