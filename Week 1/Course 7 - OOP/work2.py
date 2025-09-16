class thiet_bi:
    def __init__(self,ten,nam_sx):
        self.ten = ten
        self.nam_sx = nam_sx
class may_tinh_laptop(thiet_bi):
    def __init__(self,ten,nam_sx,RAM,HDD,Model,trang_thai):
        super().__init__(ten,nam_sx)
        self.RAM = RAM
        self.HDD = HDD
        self.Model = Model
        self.trang_thai = trang_thai
    def start(self):
        print(f"Start")
        self.trang_thai = True 
lenovo = may_tinh_laptop("Lenovo","2024","16GB","1 TB SSD","Legion","Like_New")
print(f"Thiet bi:{lenovo.ten}")
print(f"RAM: {lenovo.RAM}")
print(f"Tinh trang:{lenovo.trang_thai}")
lenovo.start()
