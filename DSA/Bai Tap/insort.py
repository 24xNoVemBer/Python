def solve():
    number = int(input())
    arr = list(map(int, input().split()))
    a = [arr[0]]
    count = 1
    print(f"Buoc 0: {arr[0]}")
    for i in range(1, number):
        kt = False
        for j in range(len(a)):
            if arr[i] <= a[j]:
                a.insert(j, arr[i])
                kt = True
                break
        if not kt:
            a.append(arr[i])
        print(f"Buoc {count}:", end=' ')
        for _ in a:
            print(_, end=' ')
        print()
        count += 1

solve()
