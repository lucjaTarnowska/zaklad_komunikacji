from tkinter import ttk 
from tkinter import * 
import tkintermapview 


class StronaMapy:
    def __init__(self):
        lista_autobusow = []
        lista_klierowcow = []
        lista_klietnow = []

        self.root = Tk() 
        self.root.resizable(False, False)
        self.root.title("Zaklad komunikacji autobusowej w Kobylce")
        self.root.geometry("1200x800")

        ramka_autobusy = Frame(self.root)
        ramka_kierowcy = Frame(self.root)
        ramka_klienci = Frame(self.root)

        ramka_autobusy.grid(row=0, column=0)
        ramka_kierowcy.grid(row=0, column=1)
        ramka_klienci.grid(row=0, column=2)

        label_lista_autobusow = Label(ramka_autobusy, text="Autobusy")
        button_pokaz_wszystkie = Button(ramka_autobusy, text="Pokaż wszystkie autobusy", width=68)
        self.listbox_lista_autobusow = Listbox(ramka_autobusy, width=80) 
        button_pokaz_autobus = Button(ramka_autobusy, text="Pokaż zaznaczony autobus")
        button_dodaj_autobus = Button(ramka_autobusy, text="Dodaj autobus")
        button_usun_autobus = Button(ramka_autobusy, text="Usuń autobus")
        button_edytuj_autobus = Button(ramka_autobusy, text="Edytuj autobus")

        label_lista_autobusow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkie.grid(row=1, column=0, columnspan=4, pady=10)
        self.listbox_lista_autobusow.grid(row=2, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_autobus.grid(row=3, column=0)
        button_dodaj_autobus.grid(row=3, column=1)
        button_usun_autobus.grid(row=3, column=2)
        button_edytuj_autobus.grid(row=3, column=3)

        self.root.mainloop()