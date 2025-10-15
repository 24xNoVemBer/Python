arr = list(map(int, input().split()))

pr_sum = []
s = arr[0]
for i in range(len(arr)):
    if i!=0:
        pr_sum[i]=pr_sum[i-1]+arr[i]
    else:
        pr_sum[0]=arr[0]
l=0
r=len(pr_sum)-1

max_sum = pr_sum[0]
while l<r:
    if pr_sum[l]>pr_sum[r]:
        max_sum = max(max_sum, pr_sum[r-l])
        l+=1
    else:
        max_sum = max(max_sum, pr_sum[r-l])
        r-=1
print(max_sum)