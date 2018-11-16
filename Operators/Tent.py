def tent(x):
    '''A function that looks a bit like mirrored ln (or a tent).'''
    return 1 - 2 * abs(x)


class Tent:
    arity = 1

    def __init__(self, e):
        self.e = e

    def __repr__(self):
        return 'Tent(%s)' % self.e

    def eval(self, x, y):
        (r, g, b) = self.e.eval(x, y)
        return tent(r), tent(g), tent(b)
