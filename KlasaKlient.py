from tkinter import ttk 
from tkinter import * 

from Lokalizacja import miejsce_na_wspolrzedne


class KlasaKlient:
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.lokalizacja = ""
        self.autobus = ""
        self.wsp_x = 0
        self.wsp_y = 0
    

    def okno_edycji_klienta(self, lista_autobusow):
        lista_do_wyboru_autobusow = []

        for aktualny_autobus in lista_autobusow:
            lista_do_wyboru_autobusow.append(aktualny_autobus.nazwa_autobusu)

        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Autobusy w Kobylce - klient")
        self.root.geometry("600x200")

        label_tytul = Label(self.root, text="Uzupelnij dane klienta")
        label_imie = Label(self.root, text="Podaj imie klienta: ")
        label_nazwisko = Label(self.root, text="Podaj nazwisko klienta: ")
        label_lokalizacja = Label(self.root, text="Podaj lokalizację klienta: ")
        label_autobus = Label(self.root, text="Wybierz autobus: ")

        self.pole_imie = Entry(self.root, width=50)
        self.pole_nazwisko = Entry(self.root, width=50)
        self.pole_lokalizacja = Entry(self.root, width=50)
        self.wybor_autobusow = ttk.Combobox(self.root, state="readonly",  values=lista_do_wyboru_autobusow, width=47)
        
        label_tytul.grid(row=0, column=0, columnspan=2)
        label_imie.grid(row=1, column=0)
        label_nazwisko.grid(row=2, column=0)
        label_lokalizacja.grid(row=3, column=0)
        label_autobus.grid(row=4, column=0)

        self.pole_imie.grid(row=1, column=1)
        self.pole_nazwisko.grid(row=2, column=1)
        self.pole_lokalizacja.grid(row=3, column=1)
        self.wybor_autobusow.grid(row=4, column=1)

        self.pole_imie.insert(0, self.imie)
        self.pole_nazwisko.insert(0, self.nazwisko)
        self.pole_lokalizacja.insert(0, self.lokalizacja)

        if self.autobus:
            for idx,  aktualny_autobus in enumerate(lista_do_wyboru_autobusow):
                if aktualny_autobus == self.autobus:
                    self.wybor_autobusow.current(idx)
                    break

        button_zapisz_klienta = Button(self.root, text="Zapisz dane", command=self.aktualizuj_klienta)
        button_zapisz_klienta.grid(row=5, column=1)
        self.root.mainloop()


    def aktualizuj_klienta(self):
        self.imie = self.pole_imie.get()
        self.nazwisko = self.pole_nazwisko.get()
        self.lokalizacja = self.pole_lokalizacja.get()
        self.autobus = self.wybor_autobusow.get()

        koordynaty = miejsce_na_wspolrzedne(self.pole_lokalizacja.get())
        self.wsp_x = koordynaty[0]
        self.wsp_y = koordynaty[1]
        self.root.destroy()
        self.root.quit()