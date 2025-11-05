test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input().strip()
    arr = s.split()
    arr_sort = []
    for item in arr:
        if item.isdigit():
            arr_sort.append(int(item))
    arr_sort.sort()
    print(*arr_sort)