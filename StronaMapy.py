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
        self.root.geometry("1370x800")


        ramka_autobusy = Frame(self.root)
        ramka_kierowcy = Frame(self.root)
        ramka_klienci = Frame(self.root)

        ramka_kierowcy.grid(row=0, column=0)
        ramka_autobusy.grid(row=0, column=1)
        ramka_klienci.grid(row=0, column=2)

        label_lista_kierowcow = Label(ramka_kierowcy, text="Kierowcy")
        button_pokaz_wszystkich_kierowcow = Button(ramka_kierowcy, text="Pokaż wszystkich kierowcow", width=58)
        self.listbox_lista_kierowcow = Listbox(ramka_kierowcy, width=70) 
        button_pokaz_kierowce = Button(ramka_kierowcy, text="Pokaż zaznaczonego kierowce")
        button_dodaj_kierowce = Button(ramka_kierowcy, text="Dodaj kierowce")
        button_usun_kierowce = Button(ramka_kierowcy, text="Usuń kierowce")
        button_edytuj_kierowce = Button(ramka_kierowcy, text="Edytuj kierowce")

        label_lista_kierowcow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkich_kierowcow.grid(row=1, column=0, columnspan=4, pady=10)
        self.listbox_lista_kierowcow.grid(row=2, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_kierowce.grid(row=3, column=0)
        button_dodaj_kierowce.grid(row=3, column=1)
        button_usun_kierowce.grid(row=3, column=2)
        button_edytuj_kierowce.grid(row=3, column=3)

        label_lista_autobusow = Label(ramka_autobusy, text="Autobusy")
        button_pokaz_wszystkie_autobusy = Button(ramka_autobusy, text="Pokaż wszystkie autobusy", width=58)
        checkbutton_ustaw_filtr = Checkbutton(ramka_autobusy, text="Filtruj po aktualnie zaznaczonym autobusie")
        self.listbox_lista_autobusow = Listbox(ramka_autobusy, width=70) 
        button_pokaz_autobus = Button(ramka_autobusy, text="Pokaż zaznaczony autobus")
        button_dodaj_autobus = Button(ramka_autobusy, text="Dodaj autobus")
        button_usun_autobus = Button(ramka_autobusy, text="Usuń autobus")
        button_edytuj_autobus = Button(ramka_autobusy, text="Edytuj autobus")

        label_lista_autobusow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkie_autobusy.grid(row=1, column=0, columnspan=4, pady=10)
        checkbutton_ustaw_filtr.grid(row=2, column=0, columnspan=4)
        self.listbox_lista_autobusow.grid(row=3, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_autobus.grid(row=4, column=0)
        button_dodaj_autobus.grid(row=4, column=1)
        button_usun_autobus.grid(row=4, column=2)
        button_edytuj_autobus.grid(row=4, column=3)

        label_lista_klientow = Label(ramka_klienci, text="Klienci")
        button_pokaz_wszystkich_klientow = Button(ramka_klienci, text="Pokaż wszystkich klientów", width=58)
        self.listbox_lista_klientow = Listbox(ramka_klienci, width=70) 
        button_pokaz_klienta = Button(ramka_klienci, text="Pokaż zaznaczonego klienta")
        button_dodaj_klienta = Button(ramka_klienci, text="Dodaj klienta")
        button_usun_klienta = Button(ramka_klienci, text="Usuń klienta")
        button_edytuj_klienta = Button(ramka_klienci, text="Edytuj klienta")

        label_lista_klientow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkich_klientow.grid(row=1, column=0, columnspan=4, pady=10)
        self.listbox_lista_klientow.grid(row=2, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_klienta.grid(row=3, column=0)
        button_dodaj_klienta.grid(row=3, column=1)
        button_usun_klienta.grid(row=3, column=2)
        button_edytuj_klienta.grid(row=3, column=3)

        self.root.mainloop()