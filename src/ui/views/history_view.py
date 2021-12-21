from tkinter import ttk,constants


from ui.builders.build_history_view import HistoryBuilder

class HistoryView:

    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        builder = HistoryBuilder(self._frame, self._handle_home)
        builder._buttons()
       

