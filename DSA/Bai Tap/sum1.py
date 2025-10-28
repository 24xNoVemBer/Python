gt_2 = []
for i in range(100):
    gt_2.append(2**i)

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    for j in range(len(gt_2)-1,-1,-1):
        if gt_2[j] <= n:
            su = (n * (n+1)) // 2
            su -= 2 * sum(gt_2[0:j+1])
            print(su)
            break
