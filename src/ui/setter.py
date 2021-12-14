class Setter:
    def __init__(self, equation, form_view, round_view, operations, settings):
        self._equation = equation
        self._round = round_view
        self._form = form_view

        self._operations = operations
        self._settings = settings
# Calculator

    def set_press(self, symbol):
        self._equation.set(self._operations.press(symbol))

    def set_equation(self):
        self._equation.set(self._operations.equal())
        self._operations.clear_expression()

    def set_clear_expression(self):
        empty = self._operations.clear_expression()
        self._equation.set(empty)

    def set_brackets(self):
        self._equation.set(self._operations.brackets())

    def set_ans(self):
        self._equation.set(self._operations.ans())
# Settings

    def set_increase_round(self):
        new_round = self._settings.increase_round()
        self._round.set(new_round)
        self._operations.change_round(new_round)

    def set_decrease_round(self):
        new_round = self._settings.decrease_round()
        self._round.set(new_round)
        self._operations.change_round(new_round)

    def set_default_round(self):
        default = self._settings.default_round()
        self._round.set(default)
        self._operations.change_round(default)

    def set_form(self):
        new_form = self._settings.switch_form()
        self._form.set(new_form)
        self._operations.change_form(new_form)
