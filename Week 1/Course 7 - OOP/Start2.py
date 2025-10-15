class Person:
    def __init__(self,ten,dia_chi):
        self.ten = ten
        self.dia_chi = dia_chi
       # self.quoc_tich = "Viet_Nam"
class SinhVien(Person):
    def __init__(self,ten,dia_chi,lop):
        super().__init__(ten,dia_chi)
        self.lop = lop

class GiangVien(Person):
    def __init__(self,ten,dia_chi,luong):
        super().__init__(ten,dia_chi)
        self.luong = luong

try:
    sinh_vien_test = SinhVien("Han","Ha_Dong","B03")
    print(sinh_vien_test.quoc_tich)
except Exception as loi:
    print("Loi chung chung ",loi)


