from tkinter import ttk, constants

from ui.builders.build_settings_view import SettingsBuilder


class SettingsView:
    def __init__(self, root, handle_home, setter, form_view, round_view):
        self._root = root
        self._frame = None
        self._handle_home = handle_home
        self._setter = setter
        self._form_view = form_view
        self._round_view = round_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        builder = SettingsBuilder(
            self._frame, self._handle_home, self._setter, self._form_view, self._round_view)
        builder._buttons()
        builder._labels()
