number = int(input())
arr = list(map(int, input().split()))

count = 1
for i in range(number-1):
    kt = False
    for j in range(number-i-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            kt = True
    if kt:
        print(f"Buoc {count}:",end=' ')
        for _ in arr:
            print(_,end=' ')
        print()
        count += 1