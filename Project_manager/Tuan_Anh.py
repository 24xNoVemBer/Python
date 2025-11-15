import sys
import os
import csv
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox,
)

UI_PATH = os.path.join(os.path.dirname(__file__), "valentino.ui")
TXT_PATH = os.path.join(os.path.dirname(__file__), "scores.txt")


def tinh_diem(cc, gk, ck):
    avg = cc * 0.1 + gk * 0.3 + ck * 0.6
    return round(avg, 2)


def xep_loai(avg):
    if avg >= 8.5:
        return "A"
    if avg >= 7.0:
        return "B"
    if avg >= 5.0:
        return "C"
    if avg >= 4.0:
        return "D"
    return "F"


def luu_diem(path, record):
    file_exists = os.path.exists(path)
    try:
        with open(path, "a", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "maSV", "maHP", "tenHP", "cc", "gk", "ck", "avg", "grade", "timestamp",
            ])
            if not file_exists:
                writer.writeheader()
            writer.writerow(record)
    except Exception as e:
        raise


def tim_sv(path, maSV):
    def lam_sach_id(s):
        return str(s).strip().lower()

    maSV_sach = lam_sach_id(maSV)

    if not os.path.exists(path):
        return None

    last = None
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)

            try:
                raw_headers = next(reader)
            except StopIteration:
                return None

            cleaned_fieldnames = [name.strip() for name in raw_headers]

            for row_list in reader:
                if not row_list:
                    continue

                raw_txt_maSV = row_list[0]
                csv_maSV_sach = lam_sach_id(raw_txt_maSV)

                if csv_maSV_sach == maSV_sach:
                    record = dict(zip(cleaned_fieldnames, row_list))
                    last = record
    except Exception as e:
        print(f"LỖI ĐỌC FILE: {e}")
        return None

    return last


class ScoreDialog(QDialog):
    LENGTH = 10
    SO_CHU_SO = 5
    SO_CHU_CAI = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(UI_PATH, self)

        # Kết nối các nút
        self.tinhdiem.clicked.connect(self.on_calculate)
        self.pushButton.clicked.connect(self.on_save)
        self.pushButton_2.clicked.connect(self.on_reset)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.on_lookup)

        #label kết quả
        self.label.setText("")
        self.lbl_grade.setText("")
        self.label_4.setText("Tên Học Phần:")
        self.label_6.setText("Điểm Trung Bình:")
        self.label_5.setText("Đánh Giá:")

    def bao_loi(self, text):
        QMessageBox.warning(self, "Lỗi", text)

    def xac_thuc_maSV(self, maSV):
        if len(maSV) != self.LENGTH:
            return False

        num_digits = sum(c.isdigit() for c in maSV)
        num_alphas = sum(c.isalpha() for c in maSV)

        if num_digits != self.SO_CHU_SO or num_alphas != self.SO_CHU_CAI:
            return False
        return True

    def parse_float_field(self, widget, name):
        text = widget.text().strip()
        if text == "":
            raise ValueError(f"{name} không được để trống")
        try:
            val = float(text)
        except Exception:
            raise ValueError(f"{name} phải là số")
        if val < 0 or val > 10:
            raise ValueError(f"{name} phải nằm trong [0, 10]")
        return val

    def on_calculate(self):
        try:
            cc = self.parse_float_field(self.le_cc, "Điểm chuyên cần")
            mid = self.parse_float_field(self.le_giua, "Điểm giữa kỳ")
            final = self.parse_float_field(self.le_cuoi, "Điểm cuối kỳ")
        except ValueError as e:
            self.bao_loi(str(e))
            return

        avg = tinh_diem(cc, mid, final)
        grade = xep_loai(avg)

        try:
            self.label.setText(str(avg))
            self.lbl_grade.setText(grade)
        except Exception:
            pass

    def on_save(self):
        # 1. Xác thực Mã sinh viên
        maSV = self.le_maSV.text().strip()
        if not self.xac_thuc_maSV(maSV):
            self.bao_loi("Mã sinh viên không hợp lệ")
            return

        # 2. Xác thực các trường văn bản khác
        maHP = self.le_maHP.text().strip()
        tenHP = self.le_tenHP.text().strip()

        if not maHP or not tenHP:
            self.bao_loi("Mã và Tên học phần không được để trống")
            return

        try:
            cc = self.parse_float_field(self.le_cc, "Điểm chuyên cần")
            mid = self.parse_float_field(self.le_giua, "Điểm giữa kỳ")
            final = self.parse_float_field(self.le_cuoi, "Điểm cuối kỳ")
        except ValueError as e:
            self.bao_loi(str(e))
            return

        avg = tinh_diem(cc, mid, final)
        grade = xep_loai(avg)

        #Lưu bản ghi
        record = {
            "maSV": maSV, "maHP": maHP, "tenHP": tenHP,
            "cc": cc, "gk": mid, "ck": final,
            "avg": avg, "grade": grade,
            "timestamp": datetime.now().isoformat(),
        }
        try:
            luu_diem(TXT_PATH, record)
        except Exception as e:
            self.bao_loi(f"Lưu thất bại: {e}")
            return

        QMessageBox.information(self, "Thành công", "Lưu điểm thành công")

    def on_reset(self):
        # Xóa hết dữ liệu
        self.le_maSV.clear()
        self.le_maHP.clear()
        self.le_tenHP.clear()
        self.le_cc.clear()
        self.le_giua.clear()
        self.le_cuoi.clear()
        self.lineEdit.clear()
        try:
            self.label.setText("")
            self.lbl_grade.setText("")
            self.label_4.setText("Tên Học Phần:")
            self.label_6.setText("Điểm Trung Bình:")
            self.label_5.setText("Đánh Giá:")
        except Exception:
            pass

    def on_lookup(self):
        maSV = self.lineEdit.text().strip()
        if not maSV:
            self.bao_loi("Nhập mã sinh viên để tra cứu")
            return

        self.label_4.setText("Tên Học Phần:")
        self.label_6.setText("Điểm Trung Bình:")
        self.label_5.setText("Đánh Giá:")

        rec = tim_sv(TXT_PATH, maSV)

        if not rec:
            QMessageBox.information(self, "Không tìm thấy", f"Không tìm thấy bản ghi nào cho mã sinh viên '{maSV}'.")
            return

        # Hiển thị kết quả tra cứu
        self.label_4.setText(f"Tên Học Phần: {rec.get('tenHP', 'N/A')}")
        self.label_6.setText(f"Điểm Trung Bình: {rec.get('avg', 'N/A')}")
        self.label_5.setText(f"Đánh Giá: {rec.get('grade', 'N/A')}")


def run_gui():
    app = QApplication(sys.argv)
    dlg = ScoreDialog()
    dlg.setWindowTitle("Tính điểm học phần")
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_gui()