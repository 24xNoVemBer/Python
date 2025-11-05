test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    count_le = 0
    count_chan = 0
    sum_le = 0
    for i in a:
        if i % 2 == 0:
            count_chan +=1
        else:
            count_le +=1
            sum_le += i
    if count_le > count_chan and sum_le%2==0:
        print('YES')
    else:
        print('NO')
