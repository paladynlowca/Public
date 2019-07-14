from tkinter.font import Font
from tkinter import *

from Board import Board
from Settings import Settings


class GameScreen(PanedWindow):
    def __init__(self, root, main_menu):
        super().__init__(master=root, height=600, width=500, bg='#222222')
        self._font_small = Font(family="Helvetica", size=16, weight="bold")
        self._root = root
        self._main_menu = main_menu
        self._settings = Settings()

        self._return = Button(master=self, text='Powrót', command=self._on_return, font=self._font_small,
                              fg='#cccccc', bg='#444444', activebackground='#666666', activeforeground='#cccccc')
        self._return.place(in_=self, x=375, y=525, width=100, height=50)

        return

    def show(self):
        self.place(in_=self._root)
        self._place_board()
        return

    def reload(self):
        self._board.destroy()
        self._place_board()
        return

    def _on_return(self):
        self._board.destroy()
        self.place_forget()
        self._main_menu.place(in_=self._root)
        return

    def _place_board(self):
        self._board = Board(self, self.reload, self._on_return)
        return
    pass
