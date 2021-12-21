from tkinter import ttk, constants

from calculator.operations import REPOSITORY


class HistoryBuilder:
    def __init__(self, frame, handle_home):
        self._frame = frame
        self._home = handle_home
        self._repository = REPOSITORY
        self.labels = self._repository._read()

    def _buttons(self):
        home1_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._home
        )
        home1_button.grid(row=1, column=0)

  
