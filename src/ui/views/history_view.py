from tkinter import ttk,constants


from calculator.operations import REPOSITORY

class HistoryView:

    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._labels = REPOSITORY._read()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        
        home_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._handle_home
        )
        home_button.grid(row=0, column=0)

        for i in range(0,len(self._labels)):
            self.labels(i)

    def labels(self, num):
        lab = ttk.Label(master=self._frame, text=self._labels[num])
        lab.grid()


