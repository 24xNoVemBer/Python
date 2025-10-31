class Calculator():
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return (a/b if b != 0 else 1)

def solve():
    calculator = Calculator()
    print(calculator.add(5,10))
    print(calculator.sub(5,10))
solve()