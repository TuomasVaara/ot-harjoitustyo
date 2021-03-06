from ui.views.calculator_view import CalculatorView
from ui.views.home_view import HomeView
from ui.views.settings_view import SettingsView
from ui.views.history_view import HistoryView

from ui.setter import Setter
from tkinter import StringVar


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

        self._expression = StringVar()
        self._fraction_decimal = StringVar()
        self._round_view = StringVar()

        self._fraction_decimal.set("Decimal")
        self._round_view.set("5")

        self._setter = Setter(
            self._expression, self._fraction_decimal, self._round_view)

    def start(self):
        self._show_home_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_home_view(self):
        self._hide_current_view()

        self._current_view = HomeView(
            self._root,
            self._show_calculator_view,
            self._root.destroy,
            self._show_settings_view,
            self._show_history_view
        )

        self._current_view.pack()

    def _show_calculator_view(self):
        self._hide_current_view()

        self._current_view = CalculatorView(
            self._root,
            self._show_home_view,
            self._expression,
            self._setter
        )

        self._current_view.pack()

    def _show_settings_view(self):
        self._hide_current_view()

        self._current_view = SettingsView(
            self._root,
            self._show_home_view,
            self._setter,
            self._fraction_decimal,
            self._round_view
        )

        self._current_view.pack()

    def _show_history_view(self):
        self._hide_current_view()

        self._current_view = HistoryView(
            self._root, 
            self._show_home_view
        )

        self._current_view.pack()