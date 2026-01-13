def g(s):
    a = s.split()
    a = [x.lower() for x in a if len(x)%2==0]
    a.sort()
    return "-".join(a)
print(g("Tin Hoc THPT Tin hoc"))