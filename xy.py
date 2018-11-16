class VariableX:
    arity = 0

    def __init__(self): pass

    def __repr__(self): return "x"

    def eval(self, x, y): return x, x, x


class VariableY:
    arity = 0

    def __init__(self): pass

    def __repr__(self): return "y"

    def eval(self, x, y): return y, y, y