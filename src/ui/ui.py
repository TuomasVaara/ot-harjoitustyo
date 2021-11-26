from ui.calculator_view import CalculatorView
from ui.exit_view import ExitView
from ui.settings_view import SettingsView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_exit_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_exit_view(self):
        self._hide_current_view()

        self._current_view = ExitView(
            self._root,
            self._show_calculator_view,
            self._root.destroy,
            self._show_settings_view
        )

        self._current_view.pack()

    def _show_calculator_view(self):
        self._hide_current_view()

        self._current_view = CalculatorView(
            self._root,
            self._show_exit_view
        )

        self._current_view.pack()

    def _show_settings_view(self):
        self._hide_current_view()

        self._current_view = SettingsView(
            self._root,
            self._show_exit_view
        )
