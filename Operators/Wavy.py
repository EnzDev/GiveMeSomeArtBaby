def wavy(x):
    '''A function that is wavyyy ~'''
    return 1 - (3*x)**2 + abs(x)**3


class Wavy:
    arity = 1

    def __init__(self, e):
        self.e = e

    def __repr__(self):
        return 'Fun(%s)' % self.e

    def eval(self, x, y):
        (r, g, b) = self.e.eval(x, y)
        return wavy(r), wavy(g), wavy(b)
