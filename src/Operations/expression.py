from fractions import Fraction
class Expression:
    def __init__(self):
        self.tuple = ()

    #Tulostaa lausekkeen#
    def expression(self, numbers: tuple, symbol:str):
        if symbol == "/":
            return f"{Fraction(numbers[0],numbers[1])}"
        return f"{numbers[0]}{symbol}{numbers[1]}"
        
   