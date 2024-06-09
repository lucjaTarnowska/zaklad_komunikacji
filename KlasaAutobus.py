from tkinter import * 

from Lokalizacja import miejsce_na_wspolrzedne

class KlasaAutobus:
    def __init__(self):
        self.nazwa_autobusu = ""
        self.lokalizacja = ""
        self.wsp_x = 0
        self.wsp_y = 0
    

    def okno_edycji_autobusu(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Autobusy w Kobylce - autobusy")
        self.root.geometry("600x200")

        label_tytul = Label(self.root, text="Uzupelnij dane autobusu")
        label_nazwa_autobusu = Label(self.root, text="Podaj nazwę autobusu: ")
        label_lokalizacja_autobusu = Label(self.root, text="Podaj lokalizację autobusu: ")

        self.pole_nazwa_autobusu = Entry(self.root, width=50)
        self.pole_lokalizacja_autobusu = Entry(self.root, width=50)
        
        label_tytul.grid(row=0, column=0, columnspan=2)
        label_nazwa_autobusu.grid(row=1, column=0)
        label_lokalizacja_autobusu.grid(row=2, column=0)

        self.pole_nazwa_autobusu.grid(row=1, column=1)
        self.pole_lokalizacja_autobusu.grid(row=2, column=1)

        self.pole_nazwa_autobusu.insert(0, self.nazwa_autobusu)
        self.pole_lokalizacja_autobusu.insert(0, self.lokalizacja)

        button_dodaj_autobus = Button(self.root, text="Zapisz dane", command=self.aktualizuj_autobus)
        button_dodaj_autobus.grid(row=3, column=1)
        self.root.mainloop()

    def aktualizuj_autobus(self):
        self.nazwa_autobusu = self.pole_nazwa_autobusu.get()
        self.lokalizacja = self.pole_lokalizacja_autobusu.get()
        koordynaty = miejsce_na_wspolrzedne(self.pole_lokalizacja_autobusu.get())
        self.wsp_x = koordynaty[0]
        self.wsp_y = koordynaty[1]
        self.root.destroy()
        self.root.quit()
