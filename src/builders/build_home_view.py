from tkinter import ttk, constants


class HomeBuilder:
    def __init__(self, frame, handle_calculator, handle_exit):
        self._frame = frame
        self._handle_calculator = handle_calculator
        self._handle_exit = handle_exit

    def _buttons(self):
        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_calculator
        )
        exit_button.grid(row=1, column=0)
        calculator_button = ttk.Button(
            master=self._frame,
            text="Calculator",
            command=self._handle_exit
        )
        calculator_button.grid(row=1, column=1)
