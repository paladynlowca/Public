from os import listdir, mkdir
from os.path import exists
from MyTkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('TrashIt')
        x, y = (int(self.winfo_screenwidth() / 2 - 425), int(self.winfo_screenheight() / 2 - 350))
        self.wm_geometry(f'{850}x{650}+{x}+{y}')
        self.config(bg='#444')
        self.wm_resizable(width=False, height=False)

        NavMenu(self)
        self.mainloop()
        return
    pass


class NavMenu(PanedWindow):
    def __init__(self, root: Window):
        super().__init__(master=root, height=650, width=200, borderwidth=1, relief="groove", bg=WIDGET_BG)
        self.place(in_=root, x=0, y=0)
        self.root = root
        MyButton(self, 25, 50, text='Nowy', command=self.new_command)
        MyButton(self, 25, 150, text='Wczytaj', command=self.load_command)
        MyButton(self, 25, 250, text='Zapisz', command=self.save_command)
        MyButton(self, 25, 550, text='Wyjście', command=self.exit_command)
    pass

    def new_command(self):
        print('nowy')
        if self.check_cake_exist():
            CakeExistPop(self, self.new_command, 'Plansza jest w trakcie tworzenia, na pewno chcesz rozpocząć nową?')
            pass
        else:
            NewCakePop(self.root)
            pass
        return

    def load_command(self):
        print('load')
        if self.check_cake_exist():
            CakeExistPop(self, self.load_command, 'Czy chcesz trawle usunąć katoalog Windows?')
            pass
        else:
            FilePop(self.root, 'load')
            pass
        return

    def save_command(self):
        FilePop(self.root, 'save')
        return

    def exit_command(self):
        print('wyjscie')
        if self.check_cake_exist():
            CakeExistPop(self, self.exit_command, 'Plansza jest w trakcie tworzenia, na pewno chcesz wyjść?')
            pass
        else:
            self.root.destroy()
            pass
        return

    def check_cake_exist(self):
        for i in self.root.winfo_children():
            if i.__class__ == Cake:
                return i
                pass
            pass
        return False
    pass


class Cake(PanedWindow):
    def __init__(self, root, x, y):
        super().__init__(master=root, height=600, width=600, bg=WIDGET_ABG)
        self.root = root
        self.size = (x, y)
        self.fields = {}
        for i in range(x):
            for j in range(y):
                self.fields[(i, j)] = Field(self, i, j)
                pass
            pass
        self.place(in_=self.root, x=225, y=25)
        return

    def __setitem__(self, key, value):
        if value:
            self.fields[(key[0], key[1])].config(bg='red')
            self.fields[(key[0], key[1])].road = True
        return

    def __getitem__(self, key):
        return self.fields[(key[0], key[1])]
    pass


class Field(PanedWindow):
    def __init__(self, root: Cake, x, y):
        self.road = False

        def to_road(event):
            if 0 < x < root.size[0] - 1 and 0 < y < root.size[1] - 1:
                self.config(bg='red')
                self.road = True
                pass
            return

        def to_wall(event):
            if 0 < x < root.size[0] - 1 and 0 < y < root.size[1] - 1:
                self.config(bg=WIDGET_BG)
                self.road = False
                pass
            return

        super().__init__(master=root, height=20, width=20, bg=WIDGET_BG, borderwidth=1, relief="groove")
        self.bind('<Button-1>', to_road)
        self.bind('<Button-3>', to_wall)
        if (x == 0 and y == 1) or (x == root.size[0] - 1 and y == root.size[1] - 2):
            self.config(bg='red')
            self.road = True
            pass
        self.grid(in_=root, row=y, column=x)


class CakeExistPop(Toplevel):
    def __init__(self, root, command, text):
        super().__init__(master=root, bg=WIDGET_BG)
        self.wm_resizable(width=False, height=False)
        self.grab_set()
        self._command = command
        self.root = root

        x, y = (int(self.winfo_screenwidth() / 2 - 225), int(self.winfo_screenheight() / 2 - 100))
        self.wm_geometry(f'{450}x{200}+{x}+{y}')

        label = Label(master=self, text=text, font=FONT_BASE, wraplength=350, bg=WIDGET_BG, fg=WIDGET_FG)
        label.place(in_=self, x=50, y=25, width=350, height=50)
        self.button_factory('Tak', self.yes_command, 1).focus_force()
        self.button_factory('Tak', self.no_command, 2)
        return

    def button_factory(self, text: str, command, position: int):
        button = Button(master=self, text=text, command=command, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BASE,
                        activebackground=BUTTON_ABG)
        button.place(x=position * 200 - 150, y=100, width=150, height=50)
        return button

    def yes_command(self):
        self.grab_release()
        self.destroy()
        self.root.check_cake_exist().destroy()
        self._command()
        return

    def no_command(self):
        self.grab_release()
        self.destroy()
        return


class NewCakePop(Toplevel):
    def __init__(self, root):
        super().__init__(bg=WIDGET_BG)
        self.wm_resizable(width=False, height=False)
        self.grab_set()
        x, y = (int(self.winfo_screenwidth() / 2 - 225), int(self.winfo_screenheight() / 2 - 125))
        self.wm_geometry(f'{450}x{250}+{x}+{y}')
        self.xw = IntVar()
        self.yw = IntVar()

        def scale_factory(min, max, label, variable, position):
            scale = Scale(master=self, from_=min, to=max, label=label, variable=variable, highlightthickness=0,
                          borderwidth=0, bg=WIDGET_BG, fg=WIDGET_FG, troughcolor=WIDGET_FG, activebackground=WIDGET_ABG,
                          orient=HORIZONTAL, length=350, font=FONT_BASE)
            scale.place(in_=self, x=50, y=position * 75 - 50)
            return
        scale_factory(13, 30, 'Szerokość', self.xw, 1)
        scale_factory(6, 30, 'Wysokość', self.yw, 2)
        b = Button(master=self, text='Utwórz', command=self.go, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BASE,
                   activebackground=BUTTON_ABG)
        b.place(in_=self, y=175, x=300, width=100, height=50)

        self.root = root
        return

    def go(self):
        Cake(self.root, self.xw.get(), self.yw.get())
        self.grab_release()
        self.destroy()
        return
    pass


class FilePop(Toplevel):
    def __init__(self, root, mode):
        super().__init__(bg=WIDGET_BG)
        self.wm_resizable(width=False, height=False)
        self.grab_set()
        x, y = (int(self.winfo_screenwidth() / 2 - 225), int(self.winfo_screenheight() / 2 - 125))
        self.wm_geometry(f'{450}x{250}+{x}+{y}')
        self.path = StringVar()
        self.root = root
        if not exists('boards'):
            mkdir('boards')
            pass
        if mode == 'save':
            if not self.check_cake_exist():
                self.destroy()
                pass
            else:
                self.input = Entry(master=self, textvariable=self.path, bg=BUTTON_BG,
                                   fg=BUTTON_FG, font=FONT_BASE)
                self.input.bind('<Return>', self.save)
                self.input.place(in_=self, width=250, x=75, y=50)
                self.input.focus_force()
                self.button = Button(master=self, text='Zapisz', command=self.save, bg=BUTTON_BG, fg=BUTTON_FG,
                                     font=FONT_BASE, activebackground=BUTTON_ABG)
                self.button.place(in_=self, y=175, x=300, width=100, height=50)
            pass
        elif mode == 'load':
            self.combo_box = ComboBox(self)
            self.button = Button(master=self, text='Otwórz', command=self.load, bg=BUTTON_BG, fg=BUTTON_FG,
                                 font=FONT_BASE, activebackground=BUTTON_ABG)
            self.button.place(in_=self, y=175, x=300, width=100, height=50)
            pass

        return

    def load(self):
        if self.combo_box.listbox.curselection():
            cake = self.check_cake_exist()
            if cake:
                # CakeExistPop(self, self.load, 'Plansza jest w trakcie tworzenia, na pewno chcesz wczytać?')
                CakeExistPop(self, self.load, 'Czy chcesz trawle usunąć katoalog Windows?')
                pass
            else:
                with open(path.expandvars('boards\\' + self.combo_box.listbox.selection_get()) + '.cake', 'rb') as file:
                    self.destroy()
                    x = int.from_bytes(file.read(1), byteorder='big', signed=True)
                    y = int.from_bytes(file.read(1), byteorder='big', signed=True)
                    cake = Cake(self.root, x, y)
                    for i in range(x):
                        for j in range(y):
                            value = int.from_bytes(file.read(1), byteorder='big', signed=True)
                            cake[i, j] = True if value == 1 else False
                            pass
                        pass
                    pass
            pass
        return

    # noinspection PyUnresolvedReferences
    def save(self, event='Nie istotne, ale musi być żeby enter działał -.-'):
        cake = self.check_cake_exist()
        if cake:
            path = 'boards\\' + self.path.get() + '.cake'
            # if exists(path):
            #     CakeExistPop(self, self.load, 'Plansza jest w trakcie tworzenia, na pewno chcesz wczytać?')
            #     pass
            with open(path, 'wb') as file:
                file.write(cake.size[0].to_bytes(1, byteorder='big', signed=True))
                file.write(cake.size[1].to_bytes(1, byteorder='big', signed=True))
                for x in range(cake.size[0]):
                    for y in range(cake.size[1]):
                        value = 1 if cake[x, y].road else 0
                        file.write(value.to_bytes(1, byteorder='big', signed=True))
                        pass
                    pass
                pass
            self.destroy()
        return

    def check_cake_exist(self):
        for i in self.root.winfo_children():
            if i.__class__ == Cake:
                return i
                pass
            pass
        return False
    pass


class PopWindow(Toplevel):
    def __init__(self):
        super().__init__()
        return
    pass


class ComboBox(PanedWindow):
    def __init__(self, root):
        super().__init__(master=root, bg=WIDGET_BG, borderwidth=0)

        self.label = Label(master=self, text='', bg=WIDGET_BG, fg=WIDGET_FG, font=FONT_SMALL)
        self.label.pack(side='top', fill='y')

        self.listbox = Listbox(self, width=40, height=5, font=FONT_SMALL, bg=WIDGET_ABG, fg=WIDGET_FG, borderwidth=0,
                               highlightthickness=0)

        def onselect(event):
            self.label.config(text=event.widget.selection_get())
            pass

        self.listbox.bind('<<ListboxSelect>>', onselect)
        self.listbox.pack(side="left", fill="y")
        self.listbox.focus_force()
        for i in listdir(r'boards'):
            name = re.search(r'\.cake', i)
            if name:
                self.listbox.insert(END, i.replace('.cake', ''))
            pass
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.place(in_=root, y=25, x=75)
        return

    def __str__(self):
        return self.listbox.selection_get()
    pass


if __name__ == '__main__':
    window = Window()
    pass
