test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr_1 = list(map(int, input().split()))
    N=int(input())
    arr_2 = list(map(int, input().split()))
    arr_chung = []
    for i in arr_1:
        if i in arr_2:
            arr_chung.append(i)
    print(*arr_chung)