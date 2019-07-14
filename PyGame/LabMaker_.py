from tkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('LabMaker')
        x, y = (int(self.winfo_screenwidth() / 2 - 425), int(self.winfo_screenheight() / 2 - 350))
        self.wm_geometry(f'{850}x{650}+{x}+{y}')
        self.config(bg='#444')
        self.wm_resizable(width=False, height=False)

        nav_menu = NavMenu(self)
        self.mainloop()
        return
    pass


class NavMenu(PanedWindow):
    def __init__(self, root: Window):
        def button_factory(text: str, command, position: int):
            button = Button(master=self, text=text, command=command, bg='silver')
            button.place(x=25, y=position * 100 - 50, width=150, height=50)
            return
        super().__init__(master=root, height=650, width=200, borderwidth=1, relief="groove", bg='#222222')
        self.place(in_=root, x=0, y=0)
        self.root = root
        button_factory('Nowy', self.new_command, 1)
        button_factory('Wyjście', self.exit_command, 6)
    pass

    def new_command(self):
        print('nowy')
        cake_exist = False
        for i in self.root.winfo_children():
            if i.winfo_name() == '!cake':
                cake_exist = True
                self.pop_cake_exist(self.new_command, i,
                                    'Plansza jest w trakcie tworzenia, na pewno chcesz rozpocząć nową?')
                pass
            pass
        if not cake_exist:
            pop(self.root)
            pass
        return

    def exit_command(self):
        print('wyjscie')
        cake_exist = False
        for i in self.root.winfo_children():
            if i.winfo_name() == '!cake':
                cake_exist = True
                self.pop_cake_exist(self.exit_command, i, 'Plansza jest w trakcie tworzenia, na pewno chcesz wyjść?')
                pass
            pass
        if not cake_exist:
            self.root.destroy()
            pass
        return

    def pop_cake_exist(self, command, cake, text):
        def button_factory(text: str, command, position: int):
            button = Button(master=top_level, text=text, command=command, bg='silver')
            button.place(x=position * 200 - 150, y=150, width=150, height=50)
            return

        def yes_command():
            top_level.destroy()
            cake.destroy()
            command()
            return

        def no_command():
            top_level.destroy()
            return

        top_level = Toplevel(master=self.root)
        x, y = (int(self.winfo_screenwidth() / 2 - 125), int(self.winfo_screenheight() / 2 - 90))
        top_level.wm_geometry(f'{450}x{250}+{x}+{y}')

        label = Label(master=top_level, text=text)
        label.place(in_=top_level, x=50, y=25, width=400, height=50)
        button_factory('Tak', yes_command, 1)
        button_factory('Nie', no_command, 2)


class Cake(PanedWindow):
    def __init__(self, root, x, y):
        super().__init__(master=root, height=600, width=600, bg='#222222')
        self.root = root
        self.fields = {}
        for i in range(x):
            for j in range(y):
                self.fields[(i, j)] = Field(self, i, j)
                pass
            pass
        self.place(in_=self.root, x=225, y=25)
        return
    pass


class Field(PanedWindow):
    def __init__(self, root, x, y):
        self.road = False

        def to_road(event):
            self.config(bg='red')
            self.road = True
            pass

        def to_wall(event):
            self.config(bg='#222222')
            self.road = False
            pass

        super().__init__(master=root, height=20, width=20, bg='#222222', borderwidth=1, relief="groove")
        self.bind('<Button-1>', to_road)
        self.bind('<Button-3>', to_wall)
        self.grid(in_=root, row=y, column=x)


class pop(Toplevel):
    def __init__(self, root):
        super().__init__()
        x, y = (int(self.winfo_screenwidth() / 2 - 125), int(self.winfo_screenheight() / 2 - 90))
        self.wm_geometry(f'{250}x{180}+{x}+{y}')
        self.xw = IntVar()
        self.yw = IntVar()
        w = Scale(master=self, length=100, label='Szerokość', from_=13, to=30, variable=self.xw)
        w.place(in_=self, x=10)
        d = Scale(master=self, length=100, label='Wysokość', from_=6, to=30, variable=self.yw)
        d.place(in_=self, x=110)
        b = Button(master=self, text='ok', command=self.go)
        b.place(in_=self, y=120, x=100)

        self.root = root
        return

    def go(self):
        cake = Cake(self.root, self.xw.get(), self.yw.get())
        self.destroy()


if __name__ == '__main__':
    window = Window()
    pass
