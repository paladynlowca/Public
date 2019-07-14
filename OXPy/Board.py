from random import Random
from tkinter import *
from tkinter.font import Font

from Settings import Settings
from Opponent import SIEasy, SIMedium
from stats import Stats


class Board(PanedWindow):
    def __init__(self, root, reload, exit):
        super().__init__(master=root, height=450, width=450,  bg='#222222', borderwidth=2, relief="groove")
        self.place(in_=root, x=25, y=25)
        self._fields = {}
        self._settings = Settings()
        if self._settings.difficulty == 1:
            self._SI = SIEasy(self)
            pass
        elif self._settings.difficulty == 2:
            self._SI = SIMedium(self)
            pass
        else:
            self._SI = SIMedium(self)
            pass
        self.status = True
        self._reload = reload
        self._exit = exit
        for i in range(3):
            for j in range(3):
                self._fields[(i, j)] = Cell(self, i, j)
                self._fields[(i, j)].bind("<Button-1>", self.onclick)
                pass
            pass
        if Random.randint(Random(), 0, 1):
            self._SI.play()
        return

    @property
    def free_count(self):
        count = 0
        for i in self._fields:
            if self._fields[i].value == 0:
                count += 1
                pass
        return count

    @property
    def free_fields(self):
        list = []
        for i in self._fields:
            if self._fields[i].value == 0:
                list.append(self._fields[i])
                pass
        return list

    def onclick(self, event):
        if self.status:
            self.set_sign('player', event.widget, "#22aa22")
        return

    def __getitem__(self, item):
        return self._fields[item]

    def set_sign(self, player, target, color):
        if player == 'player':
            sign = self._settings.sign
            pass
        else:
            sign = self._settings.sign_opponent
            pass
        result = target.draw(sign, color, True)
        if self.check_win():
            self.status = False
            pass
        if self.status and result and player == 'player':
            self._SI.play()
            pass
        return

    def check_win(self):
        def popup(event):
            _font_small = Font(family="Helvetica", size=16, weight="bold")
            if event == 'win':
                title = 'Wygrana'
                message = 'Wygrałeś!'
                pass
            elif event == 'lose':
                title = 'Przegrana'
                message = 'Przegrałeś!'
                pass
            else:
                title = 'Remis'
                message = 'Zremisowałeś!'
                pass

            pop_window = Toplevel(bg='#222222')
            x, y = (int(pop_window.winfo_screenwidth() / 2 - 125), int(pop_window.winfo_screenheight() / 2 - 90))
            pop_window.wm_geometry(f'{250}x{180}+{x}+{y}')
            pop_window.wm_title(title)
            pop_window.grab_set()
            pop_window.wm_resizable(width=False, height=False)

            def pop_new_game():
                pop_window.grab_release()
                pop_window.destroy()
                self._reload()
                return

            def pop_return():
                pop_window.grab_release()
                pop_window.destroy()
                self._exit()
                return

            pop_button_reload = Button(master=pop_window, text='Zagraj ponownie', command=pop_new_game,
                                       font=_font_small, fg='#cccccc', bg='#444444', activebackground='#666666',
                                       activeforeground='#cccccc')
            pop_button_reload.place(in_=pop_window, x=25, y=25, width=200, height=50)

            pop_button_exit = Button(master=pop_window, text='Menu główne', command=pop_return, font=_font_small,
                                     fg='#cccccc', bg='#444444', activebackground='#666666', activeforeground='#cccccc')
            pop_button_exit.place(in_=pop_window, x=25, y=100, width=200, height=50)
            return

        for i in self.check_lines(3):
            if i:
                for j in i[0]:
                    self._fields[j].draw(i[1], '#2222aa', False)
                    pass
                if i[1] == self._settings.sign:
                    popup('win')
                    Stats.add('win')
                    pass
                else:
                    popup('lose')
                    Stats.add('lose')
                    pass
                return True
                pass
            pass
        if self.free_count == 0:
            popup('pass')
            Stats.add('draw')
        return False

    def check_lines(self, number):
        def check_line(field_set):
            count = 0
            for field in field_set:
                count += self._fields[field].value
                pass
            player = 1 if self._settings.sign == 'x' else -1
            if count * player == number:
                # print('Wygrałeś')
                return field_set, self._settings.sign
                pass
            elif count * player == -number:
                # print('Przegrałeś')
                return field_set, self._settings.sign_opponent
                pass
            else:
                return False

        lines = [check_line(((0, 0), (1, 0), (2, 0))), check_line(((0, 1), (1, 1), (2, 1))),
                 check_line(((0, 2), (1, 2), (2, 2))), check_line(((0, 0), (0, 1), (0, 2))),
                 check_line(((1, 0), (1, 1), (1, 2))), check_line(((2, 0), (2, 1), (2, 2))),
                 check_line(((0, 0), (1, 1), (2, 2))), check_line(((0, 2), (1, 1), (2, 0)))]
        return lines
    pass


class Cell(Canvas):
    def __init__(self, root, i, j):
        super().__init__(master=root, height=140, width=140, bg='#222222')
        self.grid(in_=root, row=i, column=j)
        self._value = IntVar(0)
        self.value = 0

    @property
    def value(self):
        return self._value.get()

    @value.setter
    def value(self, value):
        if value not in [-1, 0, 1]:
            raise ValueError('Incorrect cell value.')
        self._value.set(value)
        return

    def draw(self, sign, color, mode):
        if self.value == 0 or not mode:
            if sign == 'x':
                self.value = 1
                self.draw_x(color)
                pass
            elif sign == 'o':
                self.value = -1
                self.draw_o(color)
                pass
            return True
        else:
            return False

    def draw_x(self, color):
        self.create_line(10, 10, 130, 130, fill=color, width=4.0)
        self.create_line(10, 130, 130, 10, fill=color, width=4.0)
        return

    def draw_o(self, color):
        self.create_oval(10, 10, 130, 130, outline=color, width=4.0)
        return
    pass
