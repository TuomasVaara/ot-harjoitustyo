from tkinter import ttk, constants


class SettingsView:

    def __init__(self, root, handle_exit):
        self._root = root
        self._handle_exit = handle_exit
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill.constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Settings")

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._handle_exit
        )

        label.grid(row=0, column=0)
        return_button.grid(row=1, column=0)
