from tkinter import ttk, constants, StringVar
from Operations.operations import Operations
from Operations.expression import Expression

class CalculatorView:

    def __init__(self, root, handle_exit):
        self._root = root
        self._handle_exit = handle_exit
        self._frame = None
        self._calculator = Operations()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Operations")

        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_exit
        )

        add_button = ttk.Button(
            master=self._frame,
            text="+"
        )
        subtract_button = ttk.Button(
            master=self._frame,
            text="-"
        )
        multiply_button = ttk.Button(
            master=self._frame,
            text="*"
        )
        divide_button = ttk.Button(
            master=self._frame,
            text="/"
        )

        label.grid(row=0, column=0)
        exit_button.grid(row=0, column=2)
        add_button.grid(row=1, column=0)
        subtract_button.grid(row=1, column=1)
        multiply_button.grid(row=2, column=0)
        divide_button.grid(row=2, column=1)
        