class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self,subject,score):
        self.grades[subject] = score
    def get_average_grade(self):
        total = sum(self.grades.values())
        num_subjects = len(self.grades)
        return total/num_subjects

    def display_transcript(self):
        print("\n================== Bảng điểm ==================")
        print(f"Tên sinh viên: {self.name}")
        print(f"MSSV: {self.student_id}")
        print("-----------------------------------------------")

        if not self.grades:
            print("Chưa có điểm nào được nhập.")
            return

        for subject, score in self.grades.items():
            print(f"Môn {subject}: {score}")

        # Gọi phương thức khác của chính đối tượng (self)
        avg = self.get_average_grade()
        print("-----------------------------------------------")
        print(f"✨ Điểm trung bình chung: {avg:.2f}")
        print("===============================================")




# Tạo một đối tượng sinh viên
student1 = Student("Trần Thị B", "SV001")

# Thêm điểm
student1.add_grade("Toán", 9)
student1.add_grade("Văn", 8)
student1.add_grade("Anh", 8.5)

# Hiển thị bảng điểm
student1.display_transcript()
# Kết quả:
# --- Bảng điểm ---
# Tên: Trần Thị B
# MSSV: SV001
# Toán: 9
# Văn: 8
# Anh: 8.5

# Lấy điểm trung bình
avg = student1.get_average_grade()
print(f"Điểm trung bình: {avg}") # Điểm trung bình: 8.5