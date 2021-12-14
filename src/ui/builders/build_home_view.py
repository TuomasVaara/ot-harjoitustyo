from tkinter import ttk, constants


class HomeBuilder:
    def __init__(self, frame, handle_calculator, handle_exit, handle_settings):
        self._frame = frame
        self._handle_calculator = handle_calculator
        self._handle_exit = handle_exit
        self._handle_settings = handle_settings

    def _buttons(self):
        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_calculator
        )
        exit_button.grid(row=0, column=0, sticky=constants.W)
        calculator_button = ttk.Button(
            master=self._frame,
            text="Calculator",
            command=self._handle_exit
        )
        calculator_button.grid(row=0, column=1, sticky=constants.W)
        settings_button = ttk.Button(
            master=self._frame,
            text="Settings",
            command=self._handle_settings
        )
        settings_button.grid(row=0, column=2, sticky=constants.W)
