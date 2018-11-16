class Product:
    arity = 2

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __repr__(self):
        return 'Product(%s, %s)' % (self.e1, self.e2)

    def eval(self, x, y):
        (r1, g1, b1) = self.e1.eval(x, y)
        (r2, g2, b2) = self.e2.eval(x, y)
        r3 = r1 * r2
        g3 = g1 * g2
        b3 = b1 * b2
        return r3, g3, b3
