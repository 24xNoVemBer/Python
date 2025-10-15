class Sinh_vien:
    def __init__(self,ho_ten,mssv,diem_tb):
        self.ho_ten = ho_ten
        self.mssv = mssv 
        self.diem_tb = diem_tb
    def xep_loai(self,diem_tb):
        if diem_tb >= 8:
            print("Gioi")
        elif diem_tb >=6.5:
            print("Kha")
        else:
            print("Trung binh")

sv1 = Sinh_vien("Han","1001",8)
sv2 = Sinh_vien("Valentino","1002",5)

sv1.xep_loai(sv1.diem_tb)
sv2.xep_loai(sv2.diem_tb)
        