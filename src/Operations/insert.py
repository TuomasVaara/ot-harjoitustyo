
class Insert:
    def __init__(self):
        self.list = []

    #Tulostaa lausekkeen#
    def expression(self, list:list, symbol:str):
        expression = f"{self.list[0]}"
        for i in range (1,len(self.list)):
            if self.list[i] == 0 and symbol == "":
                expression += f"-{str(self.list[i])}"
                continue
            expression += f"{symbol}{str(self.list[i])}"

        print(expression)
        
    #Numeroiden syöttö#
    def Inserts(self,symbol):
        Amount = int(input("How many numbers? "))
        for i in range (0,Amount):
            number = int(input("Give number. "))
            self.list.append(number)
        self.expression(self.list,symbol)
        return self.list

    #Numeroiden syöttö vähennyslaskuun#
    def Insert_sub(self):
        Amount = int(input("How many numbers? "))
        for i in range(0,Amount):
            number =(int(input("Give number. ")))
            if i == 0:
                self.list.append(number)
                continue
            self.list.append(-number)
        self.expression(self.list,"")
        return self.list

    def seperate(self):None