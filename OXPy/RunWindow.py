from tkinter import *
from tkinter.font import Font

from GameScreen import GameScreen
from OptionsMenu import OptionsMenu
from Settings import Settings
from StatsMenu import StatsMenu
from stats import Stats


class Window(Tk):
    def __init__(self):
        super().__init__()
        Settings.load()
        Stats.load()
        self.wm_title('Kółko i krzyżyk')
        x, y = (int(self.winfo_screenwidth() / 2 - 250), int(self.winfo_screenheight() / 2 - 300))
        self.wm_geometry(f'{500}x{600}+{x}+{y}')
        self.winfo_screen()
        self.wm_resizable(width=False, height=False)
        _main_menu = MainMenu(self)
        self.mainloop()
        return
    pass


class MainMenu(PanedWindow):
    def __init__(self, master):
        super().__init__(master=master, height=600, width=500, bg='#222222')
        self.root = master
        font_big = Font(family="Helvetica", size=26, weight="bold")

        self.show()
        self.options_menu = OptionsMenu(self.root, self)
        self.game_screen = GameScreen(self.root, self)
        self.stats_menu = StatsMenu(self.root, self)

        def button_factory(text, command, count):
            button = Button(master=self, text=text, command=command, font=font_big, fg='#cccccc',
                            bg='#444444', activebackground='#666666', activeforeground='#cccccc')
            button.place(in_=self, x=150, y=100 * count, width=200, height=50)
            return
        button_factory('Nowa gra', self.on_start, 1)
        button_factory('Opcje', self.on_options, 2)
        button_factory('Statystyki', self.on_stats, 3)
        button_factory('Wyjście', self.on_exit, 4)

        return

    def show(self):
        self.place(in_=self.root)
        return

    def on_start(self):
        self.place_forget()
        self.game_screen.show()
        return

    def on_options(self):
        self.place_forget()
        self.options_menu.show()
        return

    def on_stats(self):
        self.place_forget()
        self.stats_menu.show()
        return

    def on_exit(self):
        self.root.destroy()
        return
    pass


if __name__ == '__main__':
    window = Window()
    pass
