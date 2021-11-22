from Operations.insert import Insert

class Operations:
    def __init__(self):
        self.list = Insert()

    def Add(self, x, y):
        return x + y

    def Subtract(self, x,y):     
        return x - y
        
    def Multiply(self,x,y):
        return x * y

    def Divide(self,x,y):
        if y == 0:
            return 0
        return x / y

    def Power(self, number, power): None

    def Square(self, number): None

if __name__ == "__main__":
    calculator = Operations()