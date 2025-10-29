while True:
    try:
        n = input().strip()
        if n[0] == n[-1]:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break