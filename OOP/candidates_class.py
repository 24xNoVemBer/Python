class candidate:
    def __init__(self, name,dob,grade_1,grade_2,grade_3):
        self.name = name
        self.dob = dob
        self.grade_1 = float(grade_1)
        self.grade_2 = float(grade_2)
        self.grade_3 = float(grade_3)
    def solve(self):
        return  self.name +' '+ self.dob
    def sum_grades(self):
        return self.grade_1 + self.grade_2 + self.grade_3
name = input()
dob = input()
grade1 = float(input())
grade2 = float(input())
grade3 = float(input())
candidate1 = candidate(name,dob,grade1,grade2,grade3)
print(f"{candidate1.solve()} {candidate1.sum_grades():.1f}")