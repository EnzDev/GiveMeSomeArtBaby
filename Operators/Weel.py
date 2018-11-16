def well(x):
    '''A wavy function.'''
    return 1 - 2 / (1 + x * x) ** 8


class Well:
    arity = 1

    def __init__(self, e):
        self.e = e

    def __repr__(self):
        return 'Well(%s)' % self.e

    def eval(self, x, y):
        (r, g, b) = self.e.eval(x, y)
        return well(r), well(g), well(b)