import json
class income_repository:

    def __init__ (self):
        self.list = []
        self.path = "ot-harjoitustyo/src/databases/i_data.json"

    def load_file(self):
        with open(self.path) as file:
            self.list = json.load(file)
    
    def add_income(self, expense, amount):
        self.load_file()
        self.list[expense] = amount
        with open(self.path, "w") as file:
            json.dump(self.list, file)

if __name__ == "__main__":
    f = income_repository()
