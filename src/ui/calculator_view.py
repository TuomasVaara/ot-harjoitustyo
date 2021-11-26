from tkinter import ttk, constants, StringVar
from Operations.operations import Operations
from Operations.expression import Expression

class CalculatorView:

    def __init__(self, root, handle_exit):
        self._root = root
        self._handle_exit = handle_exit
        self._frame = None
        self._label_var1 = None
        self._label_var2 = None
        self._calculator = Operations()
        self._label_var1 = StringVar()
        self._label_var2 = StringVar()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()



    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        self._label_var1.set("0")
        self._label_var2.set("0")

        label = ttk.Label(master=self._frame, text="Operations")
        label1 = ttk.Label(master=self._frame, textvariable=self._label_var1)
        label2 = ttk.Label(master=self._frame, textvariable=self._label_var2)
        label_numbers = ttk.Label(master=self._frame, text="Input values")
        
        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_exit
        )

        add_button = ttk.Button(
            master=self._frame,
            text="+"
        )
        subtract_button = ttk.Button(
            master=self._frame,
            text="-"
        )
        multiply_button = ttk.Button(
            master=self._frame,
            text="*"
        )
        divide_button = ttk.Button(
            master=self._frame,
            text="/"
        )

        input_button1 = ttk.Button(
            master=self._frame,
            text="Input1",
            command = self._input1()
       )
        input_button2 = ttk.Button(
            master=self._frame,
            text="Input2",
            command =self._input2()
        )
        label.grid(row=0, column=0)
        exit_button.grid(row=0, column=2)
        add_button.grid(row=1, column=0)
        subtract_button.grid(row=1, column=1)
        multiply_button.grid(row=2, column=0)
        divide_button.grid(row=2, column=1)
        label_numbers.grid(row=3, column=1)
        input_button1.grid(row=4, column=1)
        input_button2.grid(row=4, column=3)
        label1.grid(row=4, column=0)
        label2.grid(row=4,column=2)

    def _input1(self):
        value = self._label_var1.get()
        increase_value = str(int(value)+1)
        self._label_var1.set(increase_value)

    def _input2(self):
        value = self._label_var2.get()
        increase_value = str(int(value)+1)
        self._label_var2.set(increase_value)