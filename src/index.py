from tkinter import Tk
from ui.ui import UI



def main():
    window = Tk()
    window.title("Calculator")

    _ui = UI(window)
    _ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
