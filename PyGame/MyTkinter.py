from tkinter import *
from Constants import *


class MyButton(Button):
    def __init__(self, master, x, y, height=50, width=150, **kw):
        super().__init__(master, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BASE, activebackground=BUTTON_ABG, **kw)
        self.place(in_=master, x=x, y=y, height=height, width=width)
        return
    pass
