from MyTkinter import *
from Geom import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('Kółko i krzyżyk')
        x, y = (int(self.winfo_screenwidth() / 2 - 450), int(self.winfo_screenheight() / 2 - 300))
        self.wm_geometry(f'{900}x{600}+{x}+{y}')
        self.winfo_screen()
        self.wm_resizable(width=False, height=False)
        ChooseMenu(self)
        self.mainloop()
        return
    pass


class ChooseMenu(PanedWindow):
    def __init__(self, root):
        super().__init__(master=root, height=600, width=300, bg='#222222')
        MenuButton(self, 'Trójkąr\n równoboczny', self.com_factory(EquilateralTriangle), 0, 1)
        MenuButton(self, 'Trójkąt\n równoramienny', self.com_factory(IsoscelesTriangle), 0, 2)

        MenuButton(self, 'Równoległobok', self.com_factory(Parallelogram), 0, 3)
        MenuButton(self, 'Deltoid', self.com_factory(Kite), 0, 4)
        MenuButton(self, 'Rąb', self.com_factory(Rhombus), 1, 1)
        MenuButton(self, 'Kwadrat', self.com_factory(Square), 1, 2)

        MenuButton(self, 'Pięciokąt\n foremny', self.com_factory(RegularPentagon), 1, 3)
        MenuButton(self, 'Sześciokąt\n foremny', self.com_factory(RegularHexagon), 1, 4)
        MenuButton(self, 'Ośmiokąt\n foremny', self.com_factory(RegularOctagon), 1, 5)
        self.place(in_=root)

        self.root = root
        return

    def com_factory(self, figure_name):
        def command():
            if 'fill' in self.root.children:
                self.root.children['fill'].destroy()
                pass
            figure = figure_name()
            EntryPanel(self.root, figure)
            return
        return command
    pass


Window()
