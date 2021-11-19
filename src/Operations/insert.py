
class Insert:
    def __init__(self):
        self.list = []

    #Tulostaa lausekkeen#
    def expression(self, list):
        expression = f"{self.list[0]}"
        for i in range (1,len(self.list)):
            expression += f"+{str(self.list[i])}"

        print(expression)
        
    #Numeroiden syöttö#
    def Inserts(self):
        Amount = int(input("How many numbers? "))
        for i in range (0,Amount):
            number = int(input("Give number. "))
            self.list.append(number)
        self.expression(self.list)
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
        self.expression(self.list)
        return self.list

    def seperate(self):None