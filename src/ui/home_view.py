from tkinter import ttk, constants

from builders.build_home_view import HomeBuilder

class HomeView:

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
        builder = HomeBuilder(self._frame, self._handle_exit, self._handle_calculator)
        label = ttk.Label(master=self._frame, text="Exit or Calculator")
        label.grid(row=0, column=0)
        builder._buttons()
        
        