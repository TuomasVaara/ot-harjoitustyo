
class Binds:
    def __init__(self, window):
        self._window = window
        

    def bind(self):
        self._window.bind("<1>", lambda:self._operator.press(1))
        self._window.bind("<2>", lambda:self._operator.press(2))
        self._window.bind("<3>", lambda:self._operator.press(3))
        self._window.bind("<4>", lambda:self._operator.press(4))
        self._window.bind("<5>", lambda:self._operator.press(5))
        self._window.bind("<6>", lambda:self._operator.press(6))
        self._window.bind("<7>", lambda:self._operator.press(7))
        self._window.bind("<8>", lambda:self._operator.press(8))
        self._window.bind("<9>", lambda:self._operator.press(9))
        self._window.bind("<0>", lambda:self._operator.press(0))
        self._window.bind("<+>", lambda:self._operator.press("+"))
        self._window.bind("<->", lambda:self._operator.press("-"))
        self._window.bind("<*>", lambda:self._operator.press("*"))
        self._window.bind("</>", lambda:self._operator.press("/"))
        self._window.bind("<(>", lambda:self._operator.press("("))
        self._window.bind("<)>", lambda:self._operator.press(")"))
    

