from utils import average


class Mix:
    arity = 3

    def __init__(self, w, e1, e2):
        self.w = w
        self.e1 = e1
        self.e2 = e2

    def __repr__(self):
        return 'Mix(%s, %s, %s)' % (self.w, self.e1, self.e2)

    def eval(self, x, y):
        w = 0.5 * (self.w.eval(x, y)[0] + 1.0)
        c1 = self.e1.eval(x, y)
        c2 = self.e2.eval(x, y)
        return average(c1, c2, )
