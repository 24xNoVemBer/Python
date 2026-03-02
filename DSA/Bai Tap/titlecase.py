test_case = int(input())
for t in range(test_case):
    s = input().strip()
    words = s.split()
    title_case = ' '.join(word.capitalize() for word in words)
    print(title_case)
