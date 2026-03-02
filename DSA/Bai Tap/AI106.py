test_case = int(input())
for _ in range(test_case):
    s = input()
    print("".join(dict.fromkeys(s)))    