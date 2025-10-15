def hien_thi_menu():
    print("Menu chinh:")
    print("1 - Tao_file_luu_tru")
    print("2 - Doc_file_luu_tru")
    print("3 - Xoa_file_luu_tru")
    print("4 - Thoat")
import os
import json 

while True:
    hien_thi_menu()
    try:
        option = int(input("Nhap lua chon cua ban: "))
        if option == 1 :
            ho_ten = input("Nhap ho ten: ")
            nam_sinh = int(input("Nhap nam sinh: "))
            luong_thang = input("Nhap luong thang: ")
            ho_so_nhan_vien = {
                "ho_va_ten" : ho_ten ,
                "nam_sinh" : nam_sinh ,
                "luong_thang" : luong_thang
            }
            with open("quanlynhanvien.json","w") as f:
                json.dump(ho_so_nhan_vien , f ,indent=4)
            print("Da tao file va luu ho so thanh cong")
        elif option == 2:
            with open("quanlynhanvien.json","r") as f:
                ho_so_nhan_vien = json.load(f)
                print(ho_so_nhan_vien["ho_va_ten"])
                print(ho_so_nhan_vien["nam_sinh"])
                print(ho_so_nhan_vien["luong_thang"])
        elif option == 3:
            if os.path.exists("quanlynhanvien.json"):
                os.remove("quanlynhanvien.json")
                print("da xoa thanh cong")
            else:
                print("Not found")
        elif option == 4:
            print("Chuong trinh ket thuc")
            break 
    except ValueError:
        print("Dau vao khong hop le, vui long nhap dung yeu cau")
    except FileNotFoundError:
        print("Khong tim thay file")
    except Exception as e:
        print(f"Da xay ra loi:{e}")

