from operations.budjet_operations import BudjetOperations

def main():
    print("Commands: 1 -> Add expenses, 2 -> Add income, 3 -> Show summary, 4 -> exit")
    prog = BudjetOperations()
    while True:
        command = int(input("Command:"))
        if command == 1: 
            print("Insert the name of expense and the amount.")
            expense = input("Expense ")
            amount = int(input("Amount "))
            prog.add_expenses(expense, amount)

        if command == 2: None

        if command == 3: None

        if command == 4:
            break

if __name__ == "__main__":
    main()