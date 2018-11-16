from utils import average


class Sum:
    arity = 2

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __repr__(self):
        return 'Sum(%s, %s)' % (self.e1, self.e2)

    def eval(self, x, y):
        return average(self.e1.eval(x, y), self.e2.eval(x, y))
