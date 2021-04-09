#!/usr/bin/python

# Utility functions
import datetime
import math
import random
import string
from tkinter import *
from PIL import ImageDraw, Image

# Import the operators
from Operators.Constant import Constant
from Operators.Level import Level
from Operators.Mix import Mix
from Operators.Mod import Mod
from Operators.Product import Product
from Operators.Sin import Sin
from Operators.Sum import Sum
from Operators.Tent import Tent
from Operators.Weel import Well
from Operators.Wavy import Wavy
from Operators.XY import VariableX, VariableY

from utils import rgb

operators = (VariableX, VariableY, Constant, Sum, Product, Mod, Sin, Tent, Well, Wavy, Level, Mix)

# Separate ops with arity 0 and arity > 0
operators0 = [op for op in operators if op.arity == 0]
operators1 = [op for op in operators if op.arity > 0]


def generate(k=50):
    '''Randonly generate an expession of a given size.'''
    if k <= 0:
        # We used up available size, generate a leaf of the expression tree
        op = random.choice(operators0)
        return op()
    else:
        # randomly pick an operator whose arity > 0
        op = random.choice(operators1)
        # generate subexpressions
        i = 0  # the amount of available size used up so far
        args = []  # the list of generated subexpression
        for j in sorted([random.randrange(k) for l in range(op.arity - 1)]):
            args.append(generate(j - i))
            i = j
        args.append(generate(k - 1 - i))
        return op(*args)


class Art:
    def __init__(self, size=2 ** 9, seed=None):
        _ = math.log(size, 2)  # Little checkup
        assert _ == int(_)

        if not seed:
            random.seed(None)
            seed = ''.join([random.choice(string.printable) for _ in range(random.randint(5, 15))])  # type: str

        self.start = datetime.datetime.now()
        x = seed
        self.x = x
        random.seed(x)
        self.size = size

        self.image1 = Image.new("RGB", (size, size), (255, 255, 255))
        self.drawing = ImageDraw.Draw(self.image1)

        self.art = None  # Init those vars here for PEP
        self.d = None  # Init those vars here for PEP
        self.y = None  # Init those vars here for PEP

    def redraw(self):
        self.art = generate(random.randrange(20, 150))
        self.d = 1  # *4*4*4  # current square size
        self.y = 0  # current row
        while self.d >= 1:
            draw_data = self.draw()
        return draw_data

    def draw(self):
        if self.y >= self.size:
            self.y = 0
            self.d = self.d // 4
        if self.d >= 1:
            for x in range(0, self.size, self.d):
                u = 2 * float(x + self.d / 2) / self.size - 1.0
                v = 2 * float(self.y + self.d / 2) / self.size - 1.0
                (r, g, b) = self.art.eval(u, v)
                self.drawing.point((x,
                                    self.y),
                                   rgb(r, g, b))
            self.y += self.d
            print("\r" + str((self.y * 100) / self.size) + "%", end='')
        else:
            print("\nDone with seed '%s' (Size %s)" % (self.x, self.size))
            filename = "randimg_%s_%s" % ("".join([_ for _ in self.x if _ in string.ascii_letters]), self.size)
            self.image1.save(filename + ".jpg")  # Export da shit out
            self.write_seed_name(filename)
            print("Total seconds elapsed : %s" % (datetime.datetime.now() - self.start).total_seconds())
            return {
                'seed': self.x,
                'size': self.size,
                'filename': filename
            }

    def write_seed_name(self, filename):
        seedNameFile = open(filename + ".txt", 'w')
        seedNameFile.write("%s\n" % self.x)
        seedNameFile.write("%d\n" % self.size)
        seedNameFile.flush()
        seedNameFile.close()
