def main():
    sum_fact = []
    sum_fact.append(1)
    n = int(input())
    for i in range(1,n):
        sum_fact.append(sum_fact[i-1]*(i+1))
    if n == 1:
        print(1)
    else:
        print(sum(sum_fact))
if __name__ == '__main__':
    main()