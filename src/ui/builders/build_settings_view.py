from tkinter import ttk, constants

from operations.operations import Operations

class SettingsBuilder:
    def __init__(self, frame, handle_home, operator):
        self._frame = frame
        self._handle_home = handle_home
        self._operator = operator

    def _labels(self):
        round_label = ttk.Label(
            master=self._frame,
            textvariable=self._operator._round_view
        )
        round_label.grid(row=1, column=1, sticky=constants.W)
        fraction_decimal_label = ttk.Label(
            master=self._frame,
            textvariable=self._operator._fraction_decimal
        )
        fraction_decimal_label.grid(row=1, column=3, sticky=constants.W)

    def _buttons(self):
        home_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._handle_home
        )
        home_button.grid(row=0, column=0, sticky=constants.W)
        round_button = ttk.Button(
            master=self._frame,
            text="Increase round",
            command=lambda:self._operator.increase_round()
        )
        round_button.grid(row=0, column=1, sticky=constants.W)
        default_round_button = ttk.Button(
            master=self._frame,
            text="Default round",
            command=lambda:self._operator.default_round()
        )
        default_round_button.grid(row=0, column=2, sticky=constants.W)
        switch_form_button = ttk.Button(
            master=self._frame,
            text="form",
            command=lambda:self._operator.switch_fraction_decimal()
        )
        switch_form_button.grid(row=0, column=3, sticky=constants.W)