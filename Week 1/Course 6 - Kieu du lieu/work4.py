f = open("ketqua.txt","rt")

noi_dung_file = f.read()

f.close()

chuoi = input("Nhap vao")

noi_dung_file += chuoi

f = open("ketqua.txt","wt")
f.write(noi_dung_file)
f.close()
