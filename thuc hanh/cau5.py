def chuan_hoa_ten(name: str) -> str:
    name = name.strip().lower()
    parts = name.split()
    return " ".join(word.capitalize() for word in parts)
test_cases = int(input())
for i in range(test_cases):
    s = input().strip()
    print(chuan_hoa_ten(s))
