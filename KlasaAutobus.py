from tkinter import * # import biblioteki pozwalającej wyświetlić okno edycji/kreacji autobusów.

from Lokalizacja import miejsce_na_wspolrzedne # Import funkcji zamienajacej adres na współrzędne

class KlasaAutobus:
    # Konstruktor danej klasy.
    def __init__(self):
        self.nazwa_autobusu = ""
        self.lokalizacja = ""
        self.wsp_x = 0
        self.wsp_y = 0
    
    # Dana funkcja odpowiada za wyświetlenie okna edycji danego obiektu oraz jego tworzenia. 
    def okno_edycji_autobusu(self):
        self.root = Tk() # nowe okno
        self.root.resizable(False, False) # Zablokowanie zmiany rozmiaru okna.
        self.root.title("Autobusy w Kobylce - autobusy") # Górny napis.
        self.root.geometry("600x200") # rozmiar okna.

        # Napisy na stronie
        label_tytul = Label(self.root, text="Uzupelnij dane autobusu")
        label_nazwa_autobusu = Label(self.root, text="Podaj nazwę autobusu: ")
        label_lokalizacja_autobusu = Label(self.root, text="Podaj lokalizację autobusu: ")

        # Pola ze szczegółami obiektu.
        self.pole_nazwa_autobusu = Entry(self.root, width=50)
        self.pole_lokalizacja_autobusu = Entry(self.root, width=50)
        
        # Ułożenie obiektów na stronie.
        label_tytul.grid(row=0, column=0, columnspan=2)
        label_nazwa_autobusu.grid(row=1, column=0)
        label_lokalizacja_autobusu.grid(row=2, column=0)
        self.pole_nazwa_autobusu.grid(row=1, column=1)
        self.pole_lokalizacja_autobusu.grid(row=2, column=1)

        # Jesli wczesniej byly jakies dane to wstaw je do odpowienidego pola
        self.pole_nazwa_autobusu.insert(0, self.nazwa_autobusu)
        self.pole_lokalizacja_autobusu.insert(0, self.lokalizacja)

        # Ustawienie przycisku do zapisu danych
        button_dodaj_autobus = Button(self.root, text="Zapisz dane", command=self.aktualizuj_autobus)
        button_dodaj_autobus.grid(row=3, column=1)

        # Uruchomienie okna
        self.root.mainloop()

    # Dana funkcja uruchamia się po wciśnięciu przycisku zapisu danych.
    # Dane są pobierane z pól i zapisywane. Na końcu okno jest zamykane.
    def aktualizuj_autobus(self):
        self.nazwa_autobusu = self.pole_nazwa_autobusu.get()
        self.lokalizacja = self.pole_lokalizacja_autobusu.get()
        koordynaty = miejsce_na_wspolrzedne(self.pole_lokalizacja_autobusu.get())
        self.wsp_x = koordynaty[0]
        self.wsp_y = koordynaty[1]
        self.root.destroy()
        self.root.quit()
