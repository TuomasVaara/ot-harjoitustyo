from tkinter import ttk, constants

from operations.operations import Operations

class SettingsBuilder:
    def __init__(self, frame, handle_home, operator):
        self._frame = frame
        self._handle_home = handle_home
        self._operator = operator

    def _buttons(self):
        home_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._handle_home
        )
        home_button.grid(row=0, column=0,sticky=constants.W)
        round_button = ttk.Button(
            master=self._frame,
            text="specify round (1,2,3,4)",
            command=lambda:self._operator.specify_round()
        )
        round_button.grid(row=0,column=1,sticky=constants.W)