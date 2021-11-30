from ui.calculator_view import CalculatorView
from ui.home_view import HomeView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

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
        )

        self._current_view.pack()

    def _show_calculator_view(self):
        self._hide_current_view()

        self._current_view = CalculatorView(
            self._root,
            self._show_home_view
        )

        self._current_view.pack()
