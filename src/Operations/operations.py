from Operations.insert import Insert

class Operations:
    def __init__(self):
        self.list = Insert()

    def Add(self):
        return sum(self.list.Inserts("+"))

    def Subtract(self):     
        return sum(self.list.Insert_sub())
        
    def Multiply(self):
        numbers = self.list.Inserts("*")
        multi = numbers[0]
        for i in range(1, len(numbers)):
            multi *= numbers[i]
        return multi

    def Divide(self):
        numbers = self.list.Inserts("/")
        divide = numbers[0]
        for i in range (1, len(numbers)):
            if numbers[i] == 0:
                divide = 0
                break
            divide = divide/numbers[i]
        return divide

    def Power(self, number, power): None

    def Square(self, number): None

if __name__ == "__main__":
    calculator = Operations()