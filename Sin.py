import random
import math


class Sin:
    ''' Da good old sin '''
    arity = 1

    def __init__(self, e):
        self.e = e
        self.phase = random.uniform(0, math.pi)
        self.freq = random.uniform(1.0, 6.0)

    def __repr__(self):
        return 'Sin(%g + %g * %s)' % (self.phase, self.freq, self.e)

    def eval(self, x, y):
        (r1, g1, b1) = self.e.eval(x, y)
        r2 = math.sin(self.phase + self.freq * r1)
        g2 = math.sin(self.phase + self.freq * g1)
        b2 = math.sin(self.phase + self.freq * b1)
        return r2, g2, b2
