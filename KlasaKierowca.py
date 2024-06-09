from tkinter import ttk # Import innych widgetów takich jak combobox
from tkinter import * # import biblioteki pozwalającej wyświetlić okno edycji/kreacji autobusów.

from Lokalizacja import miejsce_na_wspolrzedne # Import funkcji zamienajacej adres na współrzędne


class KlasaKierowca:
    # Konstruktor danej klasy.
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.lokalizacja = ""
        self.autobus = ""
        self.wsp_x = 0
        self.wsp_y = 0
    
    # Dana funkcja odpowiada za wyświetlenie okna edycji danego obiektu oraz jego tworzenia. 
    def okno_edycji_kierowcy(self, lista_autobusow):
        # Lista do wyboru autobusow dla Comboboxa
        lista_do_wyboru_autobusow = []

        # Przejdź po wszystkich elementach listy autobusów i dodaj do listy combobxa tylko nazwy linii
        for aktualny_autobus in lista_autobusow:
            lista_do_wyboru_autobusow.append(aktualny_autobus.nazwa_autobusu)

        self.root = Tk() # nowe okno
        self.root.resizable(False, False) # Zablokowanie zmiany rozmiaru okna.
        self.root.title("Autobusy w Kobylce - kierowca") # Górny napis.
        self.root.geometry("600x200") # rozmiar okna.

        # Napisy na stronie
        label_tytul = Label(self.root, text="Uzupelnij dane kierowcy")
        label_imie = Label(self.root, text="Podaj imie kierowcy: ")
        label_nazwisko = Label(self.root, text="Podaj nazwisko kierowcy: ")
        label_lokalizacja = Label(self.root, text="Podaj lokalizację kierowcy: ")
        label_autobus = Label(self.root, text="Wybierz autobus: ")

        # Pola ze szczegółami obiektu.
        self.pole_imie = Entry(self.root, width=50)
        self.pole_nazwisko = Entry(self.root, width=50)
        self.pole_lokalizacja = Entry(self.root, width=50)
        self.wybor_autobusow = ttk.Combobox(self.root, state="readonly",  values=lista_do_wyboru_autobusow, width=47)
        
        # Ułożenie obiektów na stronie.
        label_tytul.grid(row=0, column=0, columnspan=2)
        label_imie.grid(row=1, column=0)
        label_nazwisko.grid(row=2, column=0)
        label_lokalizacja.grid(row=3, column=0)
        label_autobus.grid(row=4, column=0)

        self.pole_imie.grid(row=1, column=1)
        self.pole_nazwisko.grid(row=2, column=1)
        self.pole_lokalizacja.grid(row=3, column=1)
        self.wybor_autobusow.grid(row=4, column=1)

        # Jesli wczesniej byly jakies dane to wstaw je do odpowienidego pola
        self.pole_imie.insert(0, self.imie)
        self.pole_nazwisko.insert(0, self.nazwisko)
        self.pole_lokalizacja.insert(0, self.lokalizacja)

        # Jeśli jest już zapisany jakiś autobus to znajdź go na liście Comboboxa i zaznacz go
        if self.autobus:
            for idx,  aktualny_autobus in enumerate(lista_do_wyboru_autobusow):
                if aktualny_autobus == self.autobus:
                    self.wybor_autobusow.current(idx)
                    break
        
        # Ustawienie przycisku do zapisu danych
        button_zapisz_kierowce = Button(self.root, text="Zapisz dane", command=self.aktualizuj_kierwoce)
        button_zapisz_kierowce.grid(row=5, column=1)

        # Uruchomienie okna
        self.root.mainloop()


    # Dana funkcja uruchamia się po wciśnięciu przycisku zapisu danych.
    # Dane są pobierane z pól i zapisywane. Na końcu okno jest zamykane.
    def aktualizuj_kierwoce(self):
        self.imie = self.pole_imie.get()
        self.nazwisko = self.pole_nazwisko.get()
        self.lokalizacja = self.pole_lokalizacja.get()
        self.autobus = self.wybor_autobusow.get()

        koordynaty = miejsce_na_wspolrzedne(self.pole_lokalizacja.get())
        self.wsp_y = koordynaty[0]
        self.wsp_x = koordynaty[1]
        self.root.destroy()
        self.root.quit()