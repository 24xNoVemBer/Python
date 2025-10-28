s = input()

s1 = s[::-1]

k = 2

str=""

for i in range(len(s1)):
    if i ==k and i!=len(s1)-1 :
        str+= s1[i]+','
        k+=3
    else:
        str+=s1[i]
print(str[::-1])