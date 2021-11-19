from Application.calculator import Calculator

def main():
    print("Commands: 1 -> exit, 2 -> calculator.")

    while True:
        Command = int(input("Command: "))

        if Command == 1:
            break
        if Command == 2:
            Calculator().calculate()


if __name__ == "__main__":
    main()