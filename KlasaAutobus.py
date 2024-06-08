from tkinter import ttk 
from tkinter import * 


class KlasaAutobus:
    def dodawanie_autobusu_okno(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Autobusy w Kobylce - dodawanie autobusu")
        self.root.geometry("600x200")

        label_tytul = Label(self.root, text="Dodawanie autobusu")
        label_nazwa_autobusu = Label(self.root, text="Podaj nazwę autobusu: ")
        label_lokalizacja_autobusu = Label(self.root, text="Podaj lokalizację autobusu: ")

        self.nazwa_autobusu = Entry(self.root, width=50)
        self.lokalizacja = Entry(self.root, width=50)
        
        label_tytul.grid(row=0, column=0, columnspan=2)
        label_nazwa_autobusu.grid(row=1, column=0)
        label_lokalizacja_autobusu.grid(row=2, column=0)

        self.nazwa_autobusu.grid(row=1, column=1)
        self.lokalizacja.grid(row=2, column=1)

        button_dodaj_autobus = Button(self.root, text="Dodaj autobus")
        button_dodaj_autobus.grid(row=3, column=1)

        self.root.mainloop()
    

    def aktualizuj_autobus(self, nazwa_autobusu, lokalizacja, wsp_x, wsp_y):
        self.nazwa_autobusu = nazwa_autobusu
        self.lokalizacja = lokalizacja
        self.wsp_x = wsp_x
        self.wsp_y = wsp_y