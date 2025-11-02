class Grade_student:
    def __init__(self, name:str, grade:list):
        self.name = name
        self.grade = grade
    def calculate_grade(self):
        return (sum(self.grade)+self.grade[1]+self.grade[0])/ (len(self.grade)+2)
class Student(Grade_student):
    count = 0
    def __init__(self, name:str, grade:list):
        super().__init__(name,grade)
        self.grade_tb = self.calculate_grade()
        Student.count += 1
        self.id = f"HS{Student.count:02d}"
    def xep_rank(self):
        if self.grade_tb >= 9:
            return 'XUAT SAC'
        elif self.grade_tb >= 8:
            return 'GIOI'
        elif self.grade_tb >= 7:
            return 'KHA'
        elif self.grade_tb >= 5:
            return 'TB'
        else:
            return 'YEU'
    def __str__(self):
        return f"{self.id} {self.name} {round(self.calculate_grade() + 1e-8, 1):.1f}"
def main():
    test_cases = int(input())
    ds = []
    for _ in range(test_cases):
        name = input().strip()
        diem = list(map(float, input().split()))
        hs = Student(name, diem)
        ds.append(hs)
    ds.sort(key=lambda x: x.grade_tb,reverse=True)
    for hs in ds:
        print(hs,hs.xep_rank())
main()