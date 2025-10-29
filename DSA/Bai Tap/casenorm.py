s = input()

ch = 0
ct = 0
for i in s:
    if i >='a' and i <='z':
        ct += 1
    else:
        ch += 1
if ct < ch:
    print(s.upper())
else:
    print(s.lower())