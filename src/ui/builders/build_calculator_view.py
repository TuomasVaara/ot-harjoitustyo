from tkinter import ttk, constants


class Builder:
    def __init__(self, frame, handle_home, setter, expression):
        self._frame = frame
        self._handle_home = handle_home
        self.equ = expression
        self._setter = setter

    def _expression(self):
        expression = ttk.Label(
            master=self._frame,
            textvariable=self.equ,
            background="white"
        )
        expression.grid(columnspan=6, ipadx=100, sticky=constants.W)

    def _numbers(self):
        num_1 = ttk.Button(
            master=self._frame,
            text="1",
            command=lambda: self._setter.set_press(1)
        )
        num_1.grid(row=1, column=0)
        num_2 = ttk.Button(
            master=self._frame,
            text="2",
            command=lambda: self._setter.set_press(2)
        )
        num_2.grid(row=1, column=1)
        num_3 = ttk.Button(
            master=self._frame,
            text="3",
            command=lambda: self._setter.set_press(3)
        )
        num_3.grid(row=1, column=2)
        num_4 = ttk.Button(
            master=self._frame,
            text="4",
            command=lambda: self._setter.set_press(4)
        )
        num_4.grid(row=1, column=3)
        num_5 = ttk.Button(
            master=self._frame,
            text="5",
            command=lambda: self._setter.set_press(5)
        )
        num_5.grid(row=1, column=4)
        num_6 = ttk.Button(
            master=self._frame,
            text="6",
            command=lambda: self._setter.set_press(6)
        )
        num_6.grid(row=2, column=0)
        num_7 = ttk.Button(
            master=self._frame,
            text="7",
            command=lambda: self._setter.set_press(7)
        )
        num_7.grid(row=2, column=1)
        num_8 = ttk.Button(
            master=self._frame,
            text="8",
            command=lambda: self._setter.set_press(8)
        )
        num_8.grid(row=2, column=2)
        num_9 = ttk.Button(
            master=self._frame,
            text="9",
            command=lambda: self._setter.set_press(9)
        )
        num_9.grid(row=2, column=3)
        num_0 = ttk.Button(
            master=self._frame,
            text="0",
            command=lambda: self._setter.set_press(0)
        )
        num_0.grid(row=2, column=4)

    def _operations(self):
        add_button = ttk.Button(
            master=self._frame,
            text="+",
            command=lambda: self._setter.set_press("+")
        )
        add_button.grid(row=3, column=0)
        subtract_button = ttk.Button(
            master=self._frame,
            text="-",
            command=lambda: self._setter.set_press("-")
        )
        subtract_button.grid(row=3, column=1)
        multiply_button = ttk.Button(
            master=self._frame,
            text="*",
            command=lambda: self._setter.set_press("*")
        )
        multiply_button.grid(row=3, column=2)
        divide_button = ttk.Button(
            master=self._frame,
            text="/",
            command=lambda: self._setter.set_press("/")
        )
        divide_button.grid(row=3, column=3)
        decimal_button = ttk.Button(
            master=self._frame,
            text=",",
            command=lambda: self._setter.set_press(".")
        )
        decimal_button.grid(row=3, column=4)
        equal_button = ttk.Button(
            master=self._frame,
            text="=",
            command=lambda: self._setter.set_equation()
        )
        equal_button.grid(row=2, column=5)
        power_button = ttk.Button(
            master=self._frame,
            text=f"x**",
            command=lambda: self._setter.set_press("**")
        )
        power_button.grid(row=4, column=0)
        sqrt_button = ttk.Button(
            master=self._frame,
            text="sqrt",
            command=lambda: self._setter.set_press("sqrt(")
        )
        sqrt_button.grid(row=4, column=1)
        log_button = ttk.Button(
            master=self._frame,
            text="ln",
            command=lambda: self._setter.set_press("log(")
        )
        log_button.grid(row=4, column=2)
        sin_button = ttk.Button(
            master=self._frame,
            text="sin",
            command=lambda: self._setter.set_press("sin(")
        )
        sin_button.grid(row=5, column=0)
        cos_button = ttk.Button(
            master=self._frame,
            text="cos",
            command=lambda: self._setter.set_press("cos(")
        )
        cos_button.grid(row=5, column=1)
        tan_button = ttk.Button(
            master=self._frame,
            text="tan",
            command=lambda: self._setter.set_press("tan(")
        )
        tan_button.grid(row=5, column=2)
        neper_button = ttk.Button(
            master=self._frame,
            text="e",
            command=lambda: self._setter.set_press("e")
        )
        neper_button.grid(row=5, column=3)
        pi_button = ttk.Button(
            master=self._frame,
            text="π",
            command=lambda: self._setter.set_press("π")
        )
        pi_button.grid(row=5, column=4)
        AC_button = ttk.Button(
            master=self._frame,
            text="AC",
            command=lambda: self._setter.set_clear_expression()
        )
        AC_button.grid(row=1, column=5)
        factorial_button = ttk.Button(
            master=self._frame,
            text="factorial",
            command=lambda: self._setter.set_press("factorial(")
        )
        factorial_button.grid(row=4, column=3)
        brackets_button = ttk.Button(
            master=self._frame,
            text="( )",
            command=lambda: self._setter.set_brackets()
        )
        brackets_button.grid(row=4, column=4)
        left_bracket_button = ttk.Button(
            master=self._frame,
            text="(",
            command=lambda: self._setter.set_press("(")
        )
        left_bracket_button.grid(row=4, column=5)
        ans_button = ttk.Button(
            master=self._frame,
            text="ans",
            command=lambda: self._setter.set_ans()
        )
        ans_button.grid(row=3, column=5)
        home_button = ttk.Button(
            master=self._frame,
            text="Home",
            command=self._handle_home
        )
        home_button.grid(row=5, column=5)
