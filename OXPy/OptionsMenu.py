from tkinter import *
from tkinter.font import Font

from Settings import Settings


class OptionsMenu(PanedWindow):
    def __init__(self, root, main_menu):
        super().__init__(master=root, height=600, width=500, bg='#222222')
        self._font_small = Font(family="Helvetica", size=16, weight="bold")
        self._root = root
        self._main_menu = main_menu
        self._settings = Settings()

        back = Button(master=self, text='Powrót', command=self._on_return, font=self._font_small,
                      fg='#cccccc', bg='#444444', activebackground='#666666', activeforeground='#cccccc')
        back.place(in_=self, x=375, y=525, width=100, height=50)

        self._place_signs()
        self._place_diff()
        return

    def show(self):
        self.place(in_=self._root)
        return

    def _on_return(self):
        self._settings.sign = self._sign_value.get()
        self._settings.difficulty = self._diff_value.get()
        Settings.save()
        self.place_forget()
        self._main_menu.place(in_=self._root)
        return

    def _place_signs(self):
        self._sign_value = StringVar(value=self._settings.sign)

        self._sings = PanedWindow(master=self, height=100, width=400, bg='#222222', borderwidth=2,
                                  relief="groove")
        self._sings.place(in_=self, x=50, y=50)

        self._signs_label = Label(master=self, text='Symbol gracza:', font=self._font_small,
                                  fg='#cccccc', bg='#222222', activebackground='#222222', activeforeground='#cccccc', )
        self._signs_label.place(in_=self._sings, x=25, y=-16)

        self._sign_x = Radiobutton(master=self._sings, variable=self._sign_value, value='x', text='x',
                                   font=self._font_small,
                                   fg='#cccccc', bg='#222222', activebackground='#222222', activeforeground='#cccccc')
        self._sign_o = Radiobutton(master=self._sings, variable=self._sign_value, value='o', text='o',
                                   font=self._font_small,
                                   fg='#cccccc', bg='#222222', activebackground='#222222', activeforeground='#cccccc')

        self._sign_x.place(in_=self._sings, x=50, y=15)
        self._sign_o.place(in_=self._sings, x=50, y=45)
        return

    def _place_diff(self):
        self._diff_value = IntVar(value=self._settings.difficulty)
        diff = PanedWindow(master=self, height=130, width=400, bg='#222222', borderwidth=2, relief="groove")
        diff.place(in_=self, x=50, y=200)

        self._signs_label = Label(master=self, text='Poziom trudności:', font=self._font_small,
                                  fg='#cccccc', bg='#222222', activebackground='#222222', activeforeground='#cccccc', )
        self._signs_label.place(in_=diff, x=25, y=-16)

        def set_rb(text, y, value):
            diff_rb = Radiobutton(master=diff, variable=self._diff_value, value=value, text=text, font=self._font_small,
                             fg='#cccccc', bg='#222222', activebackground='#222222', activeforeground='#cccccc')
            diff_rb.place(in_=diff, x=50, y=y)
        set_rb('Łatwy', 15, 1)
        set_rb('Średni', 45, 2)
        # set_rb('Trudny', 75, 3)
        return

    pass
