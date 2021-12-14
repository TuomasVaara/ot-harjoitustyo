from tkinter import ttk, constants


class SettingsBuilder:
    def __init__(self, frame, handle_home, setter, form_view, round_view):
        self._frame = frame
        self._handle_home = handle_home
        self._setter = setter
        self._form_view = form_view
        self._round_view = round_view

    def _labels(self):
        round_label = ttk.Label(
            master=self._frame,
            textvariable=self._round_view,
            background="white"
        )
        round_label.grid(row=3, column=1, sticky=constants.W)
        fraction_decimal_label = ttk.Label(
            master=self._frame,
            textvariable=self._form_view,
            background="white"
        )
        fraction_decimal_label.grid(row=1, column=2, sticky=constants.W)

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
            command=lambda: self._setter.set_increase_round()
        )
        round_button.grid(row=2, column=1, sticky=constants.W)
        round_button2 = ttk.Button(
            master=self._frame,
            text="Decrease round",
            command=lambda: self._setter.set_decrease_round()
        )
        round_button2.grid(row=1, column=1)
        default_round_button = ttk.Button(
            master=self._frame,
            text="Default round",
            command=lambda: self._setter.set_default_round()
        )
        default_round_button.grid(row=0, column=1, sticky=constants.W)
        switch_form_button = ttk.Button(
            master=self._frame,
            text="Form",
            command=lambda: self._setter.set_form()
        )
        switch_form_button.grid(row=0, column=2, sticky=constants.W)
