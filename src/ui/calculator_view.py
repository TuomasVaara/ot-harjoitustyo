from tkinter import ttk, constants, StringVar
from ui.builders.build_calculator_view import Builder


class CalculatorView:

    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._equation = StringVar()
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        builder = Builder(self._frame,self._equation)
        #Build expression 
        builder._expression()
        #Button to Home screen
        home_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._handle_home
        )
        home_button.grid(row=0, column=2)
        #Build calculator
        builder._numbers()
        builder._operations()
