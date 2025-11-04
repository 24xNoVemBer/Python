def main():
    test_cases = int(input())
    for cases in range(test_cases):
        s = input()
        max_s = 0
        res = ''
        for i in s:
            if i >='0' and i<='9':
                res += i
            else:
                max_s = max(max_s, int(res)) if res != '' else max_s
                res = ''
        max_s = max(max_s, int(res)) if res != '' else max_s
        print(max_s)
main()