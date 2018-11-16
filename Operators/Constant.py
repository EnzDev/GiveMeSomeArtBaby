import random


class Constant:
    arity = 0

    def __init__(self):
        self.c = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    def __repr__(self):
        return 'Constant(%g,%g,%g)' % self.c

    def eval(self, x, y): return self.c
