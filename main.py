#!/usr/bin/python

import random
from tkinter import *
import string

# Utility functions
import math
from PIL import ImageDraw, Image

from utils import rgb

# Import the operators
from Constant import Constant
from Level import Level
from Mix import Mix
from Mod import Mod
from Product import Product
from Sin import Sin
from Sum import Sum
from Tent import Tent
from Weel import Well
from xy import VariableX, VariableY

operators = (VariableX, VariableY, Constant, Sum, Product, Mod, Sin, Tent, Well, Level, Mix)

# We precompute those operators that have arity 0 and arity > 0
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


class DieArt:
    def __init__(self, master, size=2**12, seed=''.join(random.choices(string.ascii_uppercase + string.digits, k=15))):
        _ = math.log(size, 2)  # Little checkup
        assert _ == int(_)

        x = seed
        self.x = x
        master.title(x)
        random.seed(x)
        self.size = size
        self.canvas = Canvas(master, width=size, height=size)
        self.canvas.grid(row=0, column=0)

        self.image1 = Image.new("RGB", (size, size), (255, 255, 255))
        self.drawing = ImageDraw.Draw(self.image1)

        b = Button(master, text='Give me some sugar !', command=self.redraw)
        b.grid(row=1, column=0)
        self.draw_alarm = None
        self.redraw()

    def redraw(self):
        if self.draw_alarm: self.canvas.after_cancel(self.draw_alarm)
        self.canvas.delete(ALL)
        self.art = generate(random.randrange(20, 150))
        self.d = 1  # *4*4*4  # current square size
        self.y = 0  # current row
        self.draw()

    def draw(self):
        if self.y >= self.size:
            self.y = 0
            self.d = self.d // 4
        if self.d >= 1:
            for x in range(0, self.size, self.d):
                u = 2 * float(x + self.d / 2) / self.size - 1.0
                v = 2 * float(self.y + self.d / 2) / self.size - 1.0
                (r, g, b) = self.art.eval(u, v)
                self.canvas.create_rectangle(x,
                                             self.y,
                                             x + self.d,
                                             self.y + self.d,
                                             width=0, fill=rgb(r, g, b))
                self.drawing.point((x,
                                    self.y),
                                   rgb(r, g, b))
            self.y += self.d
            print("\r" + str((self.y * 100) / self.size) + "%", end='')
            self.draw_alarm = self.canvas.after(1, self.draw)
        else:
            self.draw_alarm = None
            filename = "randimg_%s_%s.jpg" % ("".join([_ for _ in self.x if _ in string.ascii_letters]), self.size)
            self.image1.save(filename)  # Export da shit out


# Main program
win = Tk()
win.wm_maxsize(512, 512)
arg = DieArt(win, size=512)

win.mainloop()
