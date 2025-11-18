def main():
    test_cases = int(input())
    for _ in range(test_cases):
        s = input().split()
        for i in s:
            print(i[::-1],end=' ')
        print()
if __name__ == '__main__':
    main()