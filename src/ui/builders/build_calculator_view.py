from tkinter import ttk,constants
from Operations.operations import Operations

class Builder:
    def __init__(self,frame, equation):
        self._frame = frame
        self._equ = equation
        self._operator = Operations(equation)

    def _expression(self):
        expression = ttk.Entry(
            master=self._frame,
            textvariable=self._equ
    )
        expression.grid(columnspan=3, ipadx=50)

    def _numbers(self):
        num_1 = ttk.Button(
            master=self._frame,
            text="1",
            command=lambda:self._operator.press(1)
        )
        num_1.grid(row=1,column=0)
        num_2 = ttk.Button(
            master=self._frame,
            text="2",
            command=lambda:self._operator.press(2)
        )
        num_2.grid(row=1,column=1)
        num_3 = ttk.Button(
            master=self._frame,
            text="3",
            command=lambda:self._operator.press(3)
        )
        num_3.grid(row=1,column=2)
        num_4 = ttk.Button(
            master=self._frame,
            text="4",
            command=lambda:self._operator.press(4)
        )
        num_4.grid(row=2,column=0)
        num_5 = ttk.Button(
            master=self._frame,
            text="5",
            command=lambda:self._operator.press(5)
        )
        num_5.grid(row=2,column=1)
        num_6 = ttk.Button(
            master=self._frame,
            text="6",
            command=lambda:self._operator.press(6)
        )
        num_6.grid(row=2,column=2)
        num_7 = ttk.Button(
            master=self._frame,
            text="7",
            command=lambda:self._operator.press(7)
        )
        num_7.grid(row=3,column=0)
        num_8 = ttk.Button(
            master=self._frame,
            text="8",
            command=lambda:self._operator.press(8)
        )
        num_8.grid(row=3,column=1)
        num_9 = ttk.Button(
            master=self._frame,
            text="9",
            command=lambda:self._operator.press(9)
        )
        num_9.grid(row=3,column=2)
        num_0 = ttk.Button(
            master=self._frame,
            text="0",
            command=lambda:self._operator.press(0)
        )
        num_0.grid(row=4,column=1)

    def _operations(self):
        add_button = ttk.Button(
            master=self._frame,
            text="+",
            command=lambda:self._operator.press("+")
        )
        add_button.grid(row=1, column=3)
        subtract_button = ttk.Button(
            master=self._frame,
            text="-",
            command=lambda:self._operator.press("-")
        )
        subtract_button.grid(row=2, column=3)
        multiply_button = ttk.Button(
            master=self._frame,
            text="*",
            command=lambda:self._operator.press("*")
        )
        multiply_button.grid(row=3, column=3)
        divide_button = ttk.Button(
            master=self._frame,
            text="/",
            command=lambda:self._operator.press("/")
        )
        divide_button.grid(row=4, column=3)
        decimal_button = ttk.Button(
            master=self._frame,
            text=",",
            command=lambda:self._operator.press(".")
        )
        decimal_button.grid(row=4,column=0)
        equal_button = ttk.Button(
            master=self._frame,
            text="=",
            command=lambda:self._operator.equal()
        )
        equal_button.grid(row=4, column=2)
        power_button = ttk.Button(
            master=self._frame,
            text=f"x**",
            command=lambda:self._operator.press("**")
        )
        power_button.grid(row=1, column=4)
        sqrt_button = ttk.Button(
            master=self._frame,
            text="sqrt",
            command=lambda:self._operator.power()
        )
        sqrt_button.grid(row=2, column=4)
        left_bracket_button = ttk.Button(
            master=self._frame,
            text="(",
            command=lambda:self._operator.press("(")
        )
        left_bracket_button.grid(row=5, column=0)
        right_bracket_button = ttk.Button(
            master=self._frame,
            text=")",
            command=lambda:self._operator.press(")")
        )
        right_bracket_button.grid(row=5, column=1)