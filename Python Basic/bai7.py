string = input()

nt_2 = 0
nt_3 = 0
nt_5 = 0
nt_7 = 0

for i in string:
    if i == '2':
        nt_2 += 1
    if i == '3':
        nt_3 += 1
    if i == '5':
        nt_5 += 1
    if i == '7':
        nt_7 += 1

if nt_2 !=0:
    print('2',nt_2)
if nt_3 !=0:
    print('3',nt_3)
if nt_5 !=0:
    print('5',nt_5)
if nt_7 !=0:
    print('7',nt_7)


