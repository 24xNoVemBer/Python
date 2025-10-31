class Employee():
    def __init__(self, name:str, salary:float):
        self.name = name
        self._salary = salary
    def getName(self):
        return self.name
    @property
    def getSalary(self):
        return self._salary
    def setName(self, name):
        self.name = str(name)
    def setSalary(self, salary):
        self.salary = float(salary)
    def Display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self,name:str,salary:float,bonus:int):
        super().__init__(name,salary)
        self.bonus = int(bonus)
    def getBonus(self):
            return self.bonus
    def setBonus(self, bonus):
            self.bonus = int(bonus)
    def getTotalSalary(self):
            return self.salary + self.bonus
    def Display(self):
            print(f"Name: {self.name}, Salary: {self.salary}, Bonus: {self.bonus}, Total: {self.getTotalSalary()}")
employee = Employee("Han", 300)
print(employee.getName())
print(employee.getSalary)
employee.setName("Valentino")
employee.setSalary(50000)
employee.Display()

employee_full_time = Manager("Valentino", 12000, 1000)
print(employee_full_time.getName())
print(employee_full_time.getSalary)
print(employee_full_time.getBonus())
employee_full_time.setSalary(15000)
employee_full_time.Display()
