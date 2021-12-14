from tkinter import ttk, constants
from ui.builders.build_calculator_view import Builder


class CalculatorView:

    def __init__(self, root, handle_home, expression, setter):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._expression = expression
        self._setter = setter

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        builder = Builder(self._frame, self._handle_home,
                          self._setter, self._expression)
        builder._expression()
        builder._numbers()
        builder._operations()
