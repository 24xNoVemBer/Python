class Sieunhan:
    def __init__(self,ten,mau,vu_khi):
        self.ten = "sieu nhan" + ten
        self.mau = mau
        self.vu_khi = vu_khi
    def xinchao(self):
        return "xin chao" + self.ten
a = Sieunhan("henshin","Do","Kiem")
print(a.xinchao())