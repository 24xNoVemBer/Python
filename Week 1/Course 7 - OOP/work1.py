class thiet_bi:
    def __init__(self,ten,nam_sx):
        self.ten = ten
        self.nam_sx = nam_sx
PC = thiet_bi("May_tinh_ca_nhan","2024")
print("thiet bi {} duoc san xuat nam {}".format(PC.ten,PC.nam_sx))
class laptop(thiet_bi):
    def __init__(self,ten,nam_sx,tinh_trang):
        super().__init__(ten,nam_sx)
        self.tinh_trang = tinh_trang
lenovo = laptop("Legion","2024","Like_New")
print(f"May tinh {lenovo.ten} duoc san xuat nam {lenovo.nam_sx} voi tinh trang {lenovo.tinh_trang}")