import random


class Level:
    arity = 3

    def __init__(self, level, e1, e2):
        self.threshold = random.uniform(-1.0, 1.0)
        self.level = level
        self.e1 = e1
        self.e2 = e2

    def __repr__(self):
        return 'Level(%g, %s, %s, %s)' % (self.threshold, self.level, self.e1, self.e2)

    def eval(self, x, y):
        (r1, g1, b1) = self.level.eval(x, y)
        (r2, g2, b2) = self.e1.eval(x, y)
        (r3, g3, b3) = self.e2.eval(x, y)
        r4 = r2 if r1 < self.threshold else r3
        g4 = g2 if g1 < self.threshold else g3
        b4 = b2 if b1 < self.threshold else b3
        return r4, g4, b4
