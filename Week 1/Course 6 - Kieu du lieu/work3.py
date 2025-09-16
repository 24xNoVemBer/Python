str = input("Nhap vap chuoi = ")

n = int(input("Nhap vao so N = "))

new_str = str[:n] + str[n+1:]

print(new_str)

f = open("ketqua.txt","wt")
f.write(new_str)
f.close()