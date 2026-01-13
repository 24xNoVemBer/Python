import sys
import os
import csv
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QHeaderView,
    QAbstractItemView,
    QTableWidgetItem,
)

VALENTINO_UI_PATH = os.path.join(os.path.dirname(__file__), "valentino.ui")
THONGTIN_UI_PATH = os.path.join(os.path.dirname(__file__), "thongtinsv.ui")
TXT_PATH = os.path.join(os.path.dirname(__file__), "scores.txt")
STUDENT_PATH = os.path.join(os.path.dirname(__file__), "students.txt")


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


def get_student_info(maSV):
    """Lấy thông tin sinh viên từ file students.txt"""
    if not os.path.exists(STUDENT_PATH):
        return None

    try:
        with open(STUDENT_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['maSV'].strip().lower() == maSV.strip().lower():
                    return row
    except Exception as e:
        print(f"Lỗi khi đọc file sinh viên: {e}")
    return None


def luu_diem(path, record):
    file_exists = os.path.exists(path)
    try:
        with open(path, "a", newline='', encoding='utf-8') as f:
            fieldnames = ['maSV', 'hoTen', 'maHP', 'tenHP', 'cc', 'gk', 'ck', 'avg', 'grade', 'timestamp']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
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
            reader = csv.DictReader(f)
            for row in reader:
                if lam_sach_id(row.get('maSV', '')) == maSV_sach:
                    last = row
    except Exception as e:
        print(f"LỖI ĐỌC FILE: {e}")
        return None

    return last


class StudentInfoWindow(QMainWindow):
    """Cửa sổ đăng ký thông tin sinh viên"""
    def __init__(self):
        super().__init__()
        uic.loadUi(THONGTIN_UI_PATH, self)
        self.setWindowTitle("Đăng ký thông tin sinh viên")

        # Thêm bộ xác thực đầu vào cho mã SV (chỉ chấp nhận chữ và số, tối đa 10 ký tự)
        regex = QRegExp("[A-Za-z0-9]{0,10}")
        validator = QRegExpValidator(regex)
        self.lineEdit.setValidator(validator)  # Trường Mã SV
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setPlaceholderText("VD: B25DCTN009")

        # Kết nối nút lưu - giả định pushButton là nút lưu trong thongtinsv.ui
        self.pushButton.clicked.connect(self.on_add_student)

    def on_add_student(self):
        # Lấy dữ liệu từ lineEdit, lineEdit_2, lineEdit_3
        maSV = self.lineEdit.text().strip()
        hoTen = self.lineEdit_2.text().strip()
        nganh = self.lineEdit_3.text().strip()

        if not maSV or not hoTen or not nganh:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
            return

        # Kiểm tra định dạng maSV (10 ký tự: 5 số + 5 chữ cái)
        if len(maSV) != 10:
            QMessageBox.warning(self, "Lỗi", "Mã sinh viên phải có 10 ký tự")
            return

        num_digits = sum(c.isdigit() for c in maSV)
        num_alphas = sum(c.isalpha() for c in maSV)

        if num_digits != 5 or num_alphas != 5:
            QMessageBox.warning(self, "Lỗi", "Mã sinh viên phải có 5 chữ số và 5 chữ cái")
            return

        # Kiểm tra xem sinh viên đã tồn tại chưa
        if self.student_exists(maSV):
            QMessageBox.warning(self, "Lỗi", f"Sinh viên {maSV} đã tồn tại trong hệ thống")
            return

        # Lưu thông tin sinh viên
        try:
            self.save_student(maSV, hoTen, nganh)
            QMessageBox.information(self, "Thành công", "Đã lưu thông tin sinh viên")
            self.clear_fields()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lưu: {e}")

    def student_exists(self, maSV):
        if not os.path.exists(STUDENT_PATH):
            return False

        try:
            with open(STUDENT_PATH, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['maSV'].strip().lower() == maSV.strip().lower():
                        return True
        except Exception:
            pass
        return False

    def save_student(self, maSV, hoTen, nganh):
        file_exists = os.path.exists(STUDENT_PATH)

        with open(STUDENT_PATH, 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['maSV', 'hoTen', 'nganh']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'maSV': maSV,
                'hoTen': hoTen,
                'nganh': nganh
            })

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()


class ScoreDialog(QDialog):
    LENGTH = 10
    SO_CHU_SO = 5
    SO_CHU_CAI = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(VALENTINO_UI_PATH, self)

        # Thêm bộ xác thực đầu vào cho các trường mã SV (chỉ chữ và số, tối đa 10 ký tự)
        regex = QRegExp("[A-Za-z0-9]{0,10}")
        validator = QRegExpValidator(regex)
        self.le_maSV.setValidator(validator)  # Mã SV để nhập điểm
        self.le_maSV.setMaxLength(10)
        self.le_maSV.setPlaceholderText("VD: B25DCTN009")

        self.lineEdit.setValidator(validator)  # Mã SV để tra cứu
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setPlaceholderText("VD: B25DCTN009")

        try:
            self.setup_ranking_table()
        except Exception as e:
            print("Thiết lập bảng xếp hạng bị bỏ qua hoặc thất bại:", e)

        self.tinhdiem.clicked.connect(self.on_calculate)
        self.pushButton.clicked.connect(self.on_save)
        self.pushButton_2.clicked.connect(self.on_reset)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.on_lookup)

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

        # 2. KIỂM TRA XEM SINH VIÊN CÓ TỒN TẠI KHÔNG
        student_info = get_student_info(maSV)
        if not student_info:
            self.bao_loi(
                f"Sinh viên {maSV} chưa được đăng ký trong hệ thống!\nVui lòng nhập thông tin sinh viên trước.")
            return

        # 3. Xác thực các trường văn bản khác
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

        # Lưu bản ghi (bao gồm tên sinh viên)
        record = {
            "maSV": maSV,
            "hoTen": student_info.get('hoTen', ''),
            "maHP": maHP,
            "tenHP": tenHP,
            "cc": cc,
            "gk": mid,
            "ck": final,
            "avg": avg,
            "grade": grade,
            "timestamp": datetime.now().isoformat(),
        }
        try:
            luu_diem(TXT_PATH, record)
        except Exception as e:
            self.bao_loi(f"Lưu thất bại: {e}")
            return

        QMessageBox.information(self, "Thành công", f"Lưu điểm thành công cho {student_info['hoTen']}")

        # Làm mới bảng xếp hạng sau khi lưu
        try:
            if hasattr(self, "populate_ranking_from_csv"):
                self.populate_ranking_from_csv()
        except Exception:
            pass

    def on_reset(self):
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

        self.label_4.setText(f"Tên Học Phần: {rec.get('tenHP', 'N/A')}")
        self.label_6.setText(f"Điểm Trung Bình: {rec.get('avg', 'N/A')}")
        self.label_5.setText(f"Đánh Giá: {rec.get('grade', 'N/A')}")

    def setup_ranking_table(self):
        if not hasattr(self, "tableWidget"):
            raise AttributeError("UI không có tableWidget")
        tw = self.tableWidget
        tw.setColumnCount(5)
        tw.setHorizontalHeaderLabels(["Hạng", "Mã Sinh Viên", "Họ Và Tên", "Lớp", "Điểm TB"])
        tw.verticalHeader().setVisible(False)
        tw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        tw.setAlternatingRowColors(True)
        tw.setShowGrid(False)

        header = tw.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # Hạng
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Mã SV
        header.setSectionResizeMode(2, QHeaderView.Stretch)           # Họ và Tên - mở rộng
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  # Lớp
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)  # Điểm TB

        self.apply_ranking_style()
        self.populate_ranking_from_csv()

    def populate_ranking_from_csv(self, path=TXT_PATH, top_n=10):
        if not hasattr(self, "tableWidget"):
            return
        rows = []
        if os.path.exists(path):
            try:
                with open(path, newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            avg = float(row.get('avg', 0))
                            maSV = row.get('maSV', '').strip()
                            hoTen = row.get('hoTen', '').strip()

                            # Lấy ngành (lớp) từ thông tin sinh viên
                            student_info = get_student_info(maSV)
                            nganh = student_info.get('nganh', 'N/A') if student_info else 'N/A'

                            rows.append((avg, maSV, hoTen, nganh))
                        except ValueError:
                            continue
            except Exception as e:
                print("Lỗi đọc file xếp hạng:", e)

        rows.sort(key=lambda x: x[0], reverse=True)
        rows = rows[:top_n]

        tw = self.tableWidget
        tw.setRowCount(len(rows))
        for i, (avg, maSV, hoTen, nganh) in enumerate(rows):
            # Cột 0: Xếp hạng với huy chương
            if i == 0:
                rank_text = "🥇"
            elif i == 1:
                rank_text = "🥈"
            elif i == 2:
                rank_text = "🥉"
            else:
                rank_text = str(i + 1)
            rank_item = QTableWidgetItem(rank_text)
            rank_item.setTextAlignment(Qt.AlignCenter)
            tw.setItem(i, 0, rank_item)

            # Cột 1: Mã SV
            sv_item = QTableWidgetItem(maSV)
            sv_item.setTextAlignment(Qt.AlignCenter)
            tw.setItem(i, 1, sv_item)

            # Cột 2: Họ và Tên
            name_item = QTableWidgetItem(hoTen)
            name_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            tw.setItem(i, 2, name_item)

            # Cột 3: Lớp (Ngành)
            class_item = QTableWidgetItem(nganh)
            class_item.setTextAlignment(Qt.AlignCenter)
            tw.setItem(i, 3, class_item)

            # Cột 4: Điểm TB
            score_item = QTableWidgetItem(f"{avg:.2f}")
            score_item.setTextAlignment(Qt.AlignCenter)
            tw.setItem(i, 4, score_item)

    def apply_ranking_style(self):
        if not hasattr(self, "tableWidget"):
            return
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: none;
                background-color: white;
                font-size: 13px;
                    gridline-color: #F0F0F0;
                selection-background-color: #E1F5FE;
                selection-color: black;
                alternate-background-color: #F9F9F9;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            QHeaderView::section {
                background-color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
                color: #333;
                border-bottom: 2px solid #E0E0E0;
                text-align: center;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #F0F0F0;
            }
            QTableWidget::item:alternate {
                background-color: #F9F9F9;
            }
            QTableWidget::item:selected {
                background-color: #E1F5FE;
            }
        """)


def run_gui():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0.8"

    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    # Tạo và hiển thị cửa sổ Thông tin sinh viên
    student_window = StudentInfoWindow()
    student_window.show()

    # Tạo và hiển thị cửa sổ Tính điểm
    score_window = ScoreDialog()
    score_window.setWindowTitle("Tính điểm học phần")
    score_window.show()

    # Sắp xếp các cửa sổ cạnh nhau nếu có thể
    student_window.move(100, 100)
    score_window.move(student_window.x() + student_window.width() + 20, 100)

    sys.exit(app.exec_())


if __name__ == "__main__":
    run_gui()