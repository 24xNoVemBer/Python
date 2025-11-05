test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input()
    arr = s.split()
    len_min = len(arr[0])
    save = arr[0]
    for i in arr:
        if len(i) < len_min:
            len_min = len(i)
            save = i
    print(save)