from tkinter import ttk
from tkinter import *


class StronaLogowania:

    def __init__(self):
        self.baza_uzytkownikow = {
            "lucja": "blablabla",
            "marek": "pieczarek"
        }

        # Widok okna
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Autobusy w Kobylce")
        self.root.geometry("420x200")
        napis_tytul_1 = Label(self.root, text="Aplikacja do zarzadzania autobusami w Kobylce")
        self.napis_jak_nie_wyjdzie_logowanie = Label(self.root, text="")
        napis_tytul_2 = Label(self.root, text="Dane logowania:")
        napis_login = Label(self.root, text="Login: ")
        napis_haslo = Label(self.root, text="Haslo: ")
        self.pole_login = Entry(self.root)
        self.pole_haslo = Entry(self.root, show="*")
        przycisk_do_logownia = Button(self.root, text="Zaloguj", width=17, command=self.zaloguj)
        
        napis_tytul_1.grid(row=0, column=0)
        self.napis_jak_nie_wyjdzie_logowanie.grid(row=1, column=0)
        napis_tytul_2.grid(row=2, column=0)
        napis_login.grid(row=3, column=0)
        napis_haslo.grid(row=4, column=0)
        self.pole_login.grid(row=3, column=1)
        self.pole_haslo.grid(row=4, column=1)
        przycisk_do_logownia.grid(row=5, column=1)

        self.root.mainloop()

        
    def zaloguj(self):
        if self.pole_login.get() in self.baza_uzytkownikow:
            if self.baza_uzytkownikow[self.pole_login.get()] == self.pole_haslo.get():
                self.root.destroy() # Zamknij dane okno
            else:
                self.napis_jak_nie_wyjdzie_logowanie.config(text="Podane dane sa niepoprawne", fg='#f00')
        else:
            self.napis_jak_nie_wyjdzie_logowanie.config(text="Podane dane sa niepoprawne", fg='#f00')
        