from tkinter import ttk, constants


class ExitView:

    def __init__(self, root, handle_calculator, handle_exit):
        self._root = root
        self._handle_exit = handle_exit
        self._handle_calculator = handle_calculator
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Exit or Calculator")

        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_exit
        )

        calculator_button = ttk.Button(
            master=self._frame,
            text="Calculator",
            command=self._handle_calculator
        )

        label.grid(row=0, column=0)
        exit_button.grid(row=1, column=0)
        calculator_button.grid(row=1, column=1)
        