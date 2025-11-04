a , b = map(float,input().split())

if a == 0 and b == 0:
    print("VSN")
elif b == 0 and a !=0:
    print(0)
elif a == 0 and b != 0:
    print("VN")
else:
    print(f"{(-b/a):.2f}")
