from tkinter import *
from tkinter.font import Font

from stats import Stats


class StatsMenu(PanedWindow):
    def __init__(self, root, main_menu):
        super().__init__(master=root, height=600, width=500, bg='#222222')
        self._font = Font(family="Helvetica", size=16, weight="bold")
        self._root = root
        self._main_menu = main_menu

        back = Button(master=self, text='Powrót', command=self._on_return, font=self._font,
                      fg='#cccccc', bg='#444444', activebackground='#666666', activeforeground='#cccccc')
        back.place(in_=self, x=375, y=525, width=100, height=50)

        def label_factory(text1, count):
            label1 = Label(master=self, text=text1, font=self._font, fg='#cccccc', bg='#444444', anchor='w',
                           activebackground='#666666', activeforeground='#cccccc')
            label2 = Label(master=self, text='', font=self._font, fg='#cccccc', bg='#444444', anchor='w',
                           activebackground='#666666', activeforeground='#cccccc')
            label1.place(in_=self, x=50, y=25+75*count, width=250, height=50)
            label2.place(in_=self, x=325, y=25+75*count, width=125, height=50)
            return label2

        self._all_label = label_factory(f' Mecze rozegrane: ', 1)
        self._win_label = label_factory(f' Mecze wygrane: ', 2)
        self._draw_label = label_factory(f' Mecze zremisowane: ', 3)
        self._lose_label = label_factory(f' Mecze przegrane: ', 4)
        return

    def show(self):
        self.update()
        self.place(in_=self._root)
        return

    def update(self):
        win = Stats.win
        lose = Stats.lose
        draw = Stats.draw
        all = win + draw + lose

        self._all_label.configure(text=f' {all}')
        self._win_label.configure(text=f' {win} ({win/all if all > 0 else 0:.2%})')
        self._draw_label.configure(text=f' {draw} ({draw/all if all > 0 else 0:.2%})')
        self._lose_label.configure(text=f' {lose} ({lose/all if all > 0 else 0:.2%})')
        return

    def _on_return(self):
        self.place_forget()
        self._main_menu.show()
    pass
