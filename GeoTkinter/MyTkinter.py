from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showerror
from Geom import *


class MyButton(Button):
    def __init__(self, root,  text, command, pos_x, pos_y):
        super().__init__(master=root, text=text, command=command, font=Font(family="Helvetica", size=12, weight="bold"),
                         fg='#cccccc', bg='#444444', activebackground='#666666', activeforeground='#cccccc')
        self.place(in_=root, x=pos_x, y=pos_y, width=140, height=50)
    pass


class MenuButton(MyButton):
    def __init__(self, root, text, command, collumn, row):
        super().__init__(root, text, command, 5 + collumn * 150, 100 * row - 50)
        return
    pass


class MyInsert(Entry):
    def __init__(self, root, variable, position, text):
        super().__init__(master=root, font=Font(family="Helvetica", size=12, weight="bold"), textvariable=variable,
                         fg='#cccccc', bg='#444444')
        label = MyLabel(root, text)
        label.place(in_=root, x=25, y=100 * position + 60, width=125, height=30)
        self.place(in_=root, x=175, y=100 * position + 60, width=140, height=30)
    pass


class MyLabel(Label):
    def __init__(self, root,  text):
        super().__init__(master=root, text=text, font=Font(family="Helvetica", size=11, weight="bold"), bg='#222222',
                         fg='#cccccc')
    pass


class MyListBox(Listbox):
    def __init__(self, root, pos_y):
        super().__init__(master=root, font=Font(family="Helvetica", size=11, weight="bold"), bg='#222222',
                         fg='#cccccc', height=8, exportselection=0)
        self.insert(END, "white", "black", "red", "green", "blue", "cyan", "yellow", "magenta")
        self.place(in_=root, x=350, y=pos_y + 75)


class EntryPanel(PanedWindow):
    def __init__(self, root, figure: ConvexPolygon):
        super().__init__(master=root, height=600, width=600, bg='#222222', name='fill')
        self.root = root
        self.figure = figure
        self.entries = []
        self.values = {}
        position = 0
        for entry in figure.attributes:
            self.values[entry] = Value()
            self.entries.append(MyInsert(self, self.values[entry], position, figure.attributes[entry]))
            position += 1
            pass
        self.outline_color = MyListBox(self, 0)
        self.outline_color.selection_set(1)
        self.fill_color = MyListBox(self, 200)
        self.fill_color.selection_set(0)

        MyButton(self, 'Zakończ', self.finish, 400, 500)
        self.place(in_=root, x=300)

        return

    def finish(self):
        try:
            for i in self.values:
                exec('self.figure.' + i + ' = ' + self.values[i].real.__str__())
                pass
            self.figure.check_correct()
            self.figure.outline_color = self.outline_color.curselection()
            self.figure.fill_color = self.fill_color.curselection()
            self.destroy()
            MyCanvas(self.root, self.figure)
        except ValueError:
            showerror("Błąd wartości", "Podano błędne wartości parametrów, lub nie podano ich wcale.")
            pass
        return
    pass


class MyCanvas(Canvas):
    def __init__(self, root, figure: ConvexPolygon):
        super().__init__(root, height=600, width=600, bg='#222222', name='fill', highlightbackground='#222222')
        self.figure = figure
        self.draw()
        perimeter = MyLabel(self, f'Obwód: {self.figure.perimeter():.2f}')
        perimeter.place(in_=self, x=50, y=10, width=200, height=30)
        area = MyLabel(self, f'Pole: {self.figure.area():.2f}')
        area.place(in_=self, x=350, y=10, width=200, height=30)
        self.place(in_=root, x=300)
        return

    def draw(self):
        corners = self.figure.draw()
        max_x = 0
        max_y = 0
        for c in corners:
            if c[0] > max_x:
                max_x = c[0]
                pass
            if c[1] > max_y:
                max_y = c[1]
                pass
            pass
        max_c = max(max_x, max_y)
        if max_c > 500:
            ratio = 500 / max_c
            pass
        elif max_c < 200:
            ratio = 200 / max_c
            pass
        else:
            ratio = 1
            pass
        add_x = 0 if max_x > 500 else 150 if max_x < 200 else (500 - max_x) / 2
        add_y = 0 if max_y > 500 else 150 if max_y < 200 else (500 - max_y) / 2
        print(max_x, add_x)
        corners_new = []
        for c in corners:
            corners_new.append((c[0] * ratio + 50 + add_x, c[1] * ratio + 75 + add_y))
            pass
        self.create_polygon(corners_new, fill=self.figure.fill_color, outline=self.figure.outline_color)
        return
    pass


class Value(StringVar):
    @property
    def text(self):
        return self.get()

    @property
    def real(self):
        self.set(self.get().replace(',', '.'))
        try:
            value = float(self.get())
            pass
        except ValueError:
            raise ValueError('id - Incorrect data')
        if value <= 0:
            raise ValueError('id - Incorrect data')
        return value
    pass
