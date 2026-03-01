def count_lucky_numbers(n):
    count = 0
    for i in n:
        if i=='4' or i=='7':
            count += 1
    return count

while True:
    try:
        x = input().strip()
        if count_lucky_numbers(x)=='4' or count_lucky_numbers(x)=='7':
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
