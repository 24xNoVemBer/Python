class Product():
    TAX_RATE = 0.1
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_final_price(self):
        return self.price * (1+self.TAX_RATE)
    @classmethod
    def from_csv_string(cls,data_string):
        cls.name = data_string.split(',')[0]
        cls.price = float(data_string.split(',')[1])
        return cls(cls.name,cls.price)
    @classmethod
    def change_tax_rate(cls,new_tax_rate):
        cls.TAX_RATE = new_tax_rate
# 1. Tạo đối tượng theo cách thông thường
product_A = Product("Màn hình", 300)
print(f"Giá cuối của Product A: {product_A.get_final_price()}")
# Kết quả: 330.0 (300 + 10% thuế)

# 2. Tạo đối tượng bằng Class Method (Factory Method)
csv_data = "Chuột không dây,25.5"
product_B = Product.from_csv_string(csv_data)
print(f"Tên Product B: {product_B.name}, Giá cuối: {product_B.get_final_price()}")
# Kết quả: Tên Product B: Chuột không dây, Giá cuối: 28.05

# 3. Thay đổi thuộc tính lớp bằng Class Method
Product.change_tax_rate(0.05) # Giảm thuế xuống còn 5%
print("\nĐÃ THAY ĐỔI THUẾ SUẤT LỚP XUỐNG 5%")

# 4. Kiểm tra lại giá của các sản phẩm cũ và mới
product_C = Product("Bàn phím", 75)
print(f"Giá cuối của Product A (cũ): {product_A.get_final_price()}") # Vẫn tính theo thuế mới
print(f"Giá cuối của Product C (mới): {product_C.get_final_price()}")