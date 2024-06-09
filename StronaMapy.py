from tkinter import * # Import biblioteki graficznej
import tkintermapview # Import mapy

# Import funkcji odpowiedzialnej za zamianę adresów na lokalizację i na odwrót 
from Lokalizacja import miejsce_na_wspolrzedne, wspolrzedne_na_miejsce

# Import własnych klas
from KlasaAutobus import KlasaAutobus
from KlasaKierowca import KlasaKierowca
from KlasaKlient import KlasaKlient

class StronaMapy:
    # Konstruktor danej klasy
    def __init__(self):
        # Listy zawierające wszystkie obiekty klas autobusów, kierowców oraz klientów
        self.lista_autobusow = list()
        self.lista_kierowcow = list()
        self.lista_klietnow = list()
        # Zmienna zapobiegająca nadmiernemu odświeżaniu obiektów na stronie
        self.ostatni_status_filtru_autobusow = False

        root = Tk() # Utworzenie okna logowania.
        root.resizable(False, False) # Zablokowanie zmiany rozmiaru okna.
        root.title("Zaklad komunikacji autobusowej w Kobylce") # Tytuł na górej belce okna.
        root.geometry("1370x800") # Rozmiar okna

        # Zmienna która jest zmieniana wraz ze zmianą statusu CheckBotton. 
        # Dzięki niej wiemy czy filtr autobusów jest włączony czy wyłączony.
        self.czy_filtr_jest_wlaczony = IntVar()

        # Ramki na stronie dla łatwiejszego rozłożenia elementów na stronie
        ramka_autobusy = Frame(root)
        ramka_kierowcy = Frame(root)
        ramka_klienci = Frame(root)
        ramka_mapa = Frame(root)

        # Ustawienie położenia ramek na stronie
        ramka_kierowcy.grid(row=0, column=0)
        ramka_autobusy.grid(row=0, column=1)
        ramka_klienci.grid(row=0, column=2)
        ramka_mapa.grid(row=1, column=0, columnspan=3, pady=15)

        # Kolejne elementy na stronie dla Kierowców
        label_lista_kierowcow = Label(ramka_kierowcy, text="Kierowcy")
        button_pokaz_wszystkich_kierowcow = Button(ramka_kierowcy, text="Pokaż wszystkich kierowcow", width=58, command=self.pokaz_wszystkich_kierowcow)
        self.listbox_lista_kierowcow = Listbox(ramka_kierowcy, width=70) 
        button_pokaz_kierowce = Button(ramka_kierowcy, text="Pokaż zaznaczonego kierowce", command=self.pokaz_wybranego_kierowce)
        button_dodaj_kierowce = Button(ramka_kierowcy, text="Dodaj kierowce", command=self.dodaj_kierowce)
        button_usun_kierowce = Button(ramka_kierowcy, text="Usuń kierowce", command=self.usun_kierowce)
        button_edytuj_kierowce = Button(ramka_kierowcy, text="Edytuj kierowce", command=self.edytuj_kierowce)

        label_lista_kierowcow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkich_kierowcow.grid(row=1, column=0, columnspan=4, pady=10)
        self.listbox_lista_kierowcow.grid(row=2, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_kierowce.grid(row=3, column=0)
        button_dodaj_kierowce.grid(row=3, column=1)
        button_usun_kierowce.grid(row=3, column=2)
        button_edytuj_kierowce.grid(row=3, column=3)

        # Kolejne elementy na stronie dla Autobusów
        label_lista_autobusow = Label(ramka_autobusy, text="Autobusy")
        button_pokaz_wszystkie_autobusy = Button(ramka_autobusy, text="Pokaż wszystkie autobusy", width=58, command=self.pokaz_wszystkie_autobusy)
        checkbutton_ustaw_filtr = Checkbutton(ramka_autobusy, text="Filtruj po aktualnie zaznaczonym autobusie", onvalue=True, offvalue=False,
                                              variable=self.czy_filtr_jest_wlaczony, command=self.zmien_filtr)
        self.listbox_lista_autobusow = Listbox(ramka_autobusy, width=70) 
        button_pokaz_autobus = Button(ramka_autobusy, text="Pokaż zaznaczony autobus", command=self.pokaz_wybrany_autobus)
        button_dodaj_autobus = Button(ramka_autobusy, text="Dodaj autobus", command=self.dodaj_autobus)
        button_usun_autobus = Button(ramka_autobusy, text="Usuń autobus", command=self.usun_autobus)
        button_edytuj_autobus = Button(ramka_autobusy, text="Edytuj autobus", command=self.edytuj_autobus)
        # Podpięcie wydarzenia które jest generowane podczas kliknięcia w listę autobusów
        self.listbox_lista_autobusow.bind("<<ListboxSelect>>", self.zmien_filtr)

        label_lista_autobusow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkie_autobusy.grid(row=1, column=0, columnspan=4, pady=10)
        checkbutton_ustaw_filtr.grid(row=2, column=0, columnspan=4)
        self.listbox_lista_autobusow.grid(row=3, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_autobus.grid(row=4, column=0)
        button_dodaj_autobus.grid(row=4, column=1)
        button_usun_autobus.grid(row=4, column=2)
        button_edytuj_autobus.grid(row=4, column=3)

        # Kolejne elementy na stronie dla Klientów autobusów
        label_lista_klientow = Label(ramka_klienci, text="Klienci")
        button_pokaz_wszystkich_klientow = Button(ramka_klienci, text="Pokaż wszystkich klientów", width=58, command=self.pokaz_wszystkich_klientow)
        self.listbox_lista_klientow = Listbox(ramka_klienci, width=70) 
        button_pokaz_klienta = Button(ramka_klienci, text="Pokaż zaznaczonego klienta", command=self.pokaz_wybranego_klienta)
        button_dodaj_klienta = Button(ramka_klienci, text="Dodaj klienta", command=self.dodaj_klienta)
        button_usun_klienta = Button(ramka_klienci, text="Usuń klienta", command=self.usun_klienta)
        button_edytuj_klienta = Button(ramka_klienci, text="Edytuj klienta", command=self.edytuj_klienta)

        label_lista_klientow.grid(row=0, column=0, columnspan=4)
        button_pokaz_wszystkich_klientow.grid(row=1, column=0, columnspan=4, pady=10)
        self.listbox_lista_klientow.grid(row=2, column=0, columnspan=4, padx=15, pady=10)
        button_pokaz_klienta.grid(row=3, column=0)
        button_dodaj_klienta.grid(row=3, column=1)
        button_usun_klienta.grid(row=3, column=2)
        button_edytuj_klienta.grid(row=3, column=3)

        # Załadowanie wcześniej zdefiniowanych kierowców autobusów i klientów
        self.wstepne_dane()

        # Załadnowanie mapy oraz ustawienie jej parametrów
        self.map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1340, height=430)
        self.map_widget.set_position(52.2, 21.0)
        self.map_widget.set_zoom(8)
        self.map_widget.grid(row=0, column=0)
        # Wydarzenie które uruchamia się po naciśnięciu prawym przyciskiem na mapie.
        self.map_widget.add_right_click_menu_command(label="Dodaj nowy autobus",
                                        command=self.dodaj_autobus,
                                        pass_coords=True)

        # Pokazanie danego okna
        root.mainloop()
         
    # Dana funkcja służy do zmiany filtracji obiektów na stronie.
    # Została ona przewidziana w dwóch wariantach.
    # Pierwszym z nich jest sytuacja kiedy zaznaczona jest lub odznaczona filtracja.
    # W tym przypadku nie jest otrzymywany obiekt typu event.
    # W drugim przypadku kiedy zostanie kliknięty autobus na liście to wywoła się wydarzenie które dostarczy nam obiekt typu event.
    # W danym obiekcie znajduje się informacja jaki został wybrany element.
    def zmien_filtr(self, zdarzenie_klikniecia_wyboru_autobusow = None):
        # Część funkcji dla wyłączonego filtru

        # Na początku sprawdzane jest czy filtracja jest załączona.
        # Jeśli teraz jest załączona, a ostatnio nie była to odśwież widok i wyjdź z funkcji.
        if not self.czy_filtr_jest_wlaczony.get() and self.ostatni_status_filtru_autobusow:
            self.ostatni_status_filtru_autobusow = False
            self.uaktalnij_dane()
            return
        # Jeśli teraz filtracja jest wyłączona, a poprzednio też była wyłączona to zakończ działanie funkcji.
        elif not self.czy_filtr_jest_wlaczony.get():
            return
        
        # Część funkcji z załączonym filtrem
        self.ostatni_status_filtru_autobusow = True # Ustaw aktalny status filtru

        # Jeśli został dostarczony obiekt typu event to zbierz z niego dane.
        if zdarzenie_klikniecia_wyboru_autobusow:
            w = zdarzenie_klikniecia_wyboru_autobusow.widget # Pobranie właściwego obiektu z wydarzenia

            # Sprawdź czy teraz jest zaznaczony przynajmniej jeden obiekt. Jeśli nic nie jest zaznaczone to wyjdź z funkcji.
            if len(w.curselection()) < 1:
                return
            
            # Pobierz ID wybranego pierwszego elementu oraz nazwę autobusu.
            aktualnie_wybarny_autobus_index = int(w.curselection()[0])
            aktualnie_wybarny_autobus_text = str(w.get(aktualnie_wybarny_autobus_index)).split(" , ")[0]
        # Jeśli do funkcji nie został dostarczony obiekt to pobierz aktualnie zaznaczony obiekt.
        else:
            aktualnie_wybarny_autobus_index = self.listbox_lista_autobusow.index(ACTIVE)
            aktualnie_wybarny_autobus_text = str(self.listbox_lista_autobusow.get(ACTIVE)).split(" , ")[0]

        # Odśwież dane wraz z załączonym filtrem na wcześniej wyselekcjonowany autobus.
        self.uaktalnij_dane(aktualnie_wybarny_autobus_text)
        # Dla lepszego efektu zaznacz też na listBox zaznacz aktualnie używany autobus do filtru.
        self.listbox_lista_autobusow.select_set(aktualnie_wybarny_autobus_index)
        # Usuń wszystkie znaczki na mapie.
        self.map_widget.delete_all_marker()


    # Funkcja odpowiada za odświeżenie listboxów na aktualnym widoku.
    # Jest przewidziana w dwóch wariantach. 
    # Pierwszy z nich to brak ustawionego filtru na autobus.
    # w drugim jest dostarczona nazwa autobusu do filtracji.
    def uaktalnij_dane(self, aktualnie_wybarny_autobus_text = None):
        # Jeśli nie został podany obiekt do filtracji to pobierz co jest aktualnie zaznaczone w listbox autobusów.
        if not aktualnie_wybarny_autobus_text:
            aktualnie_wybarny_autobus_text = str(self.listbox_lista_autobusow.get(ACTIVE)).split(" , ")[0]

        # Wyczyść wszystkie listy na oknie.
        self.listbox_lista_autobusow.delete(0, END)
        self.listbox_lista_kierowcow.delete(0, END)
        self.listbox_lista_klientow.delete(0, END)
        
        # Uzupełnij listę autobusów w listboxie
        for idx, aktualny_autobus in enumerate(self.lista_autobusow):
            self.listbox_lista_autobusow.insert(idx, f'{aktualny_autobus.nazwa_autobusu} , {aktualny_autobus.lokalizacja}')

        # Uzupełnij listę kierowców w listboxie. Jeśli jest załączony filtr to odfiltruj pasujących.
        for idx, aktualny_kierowca in enumerate(self.lista_kierowcow):
            if not self.czy_filtr_jest_wlaczony.get() or aktualny_kierowca.autobus == aktualnie_wybarny_autobus_text:
                self.listbox_lista_kierowcow.insert(idx, f'{aktualny_kierowca.imie} {aktualny_kierowca.nazwisko}, '
                                                f'{aktualny_kierowca.lokalizacja}, {aktualny_kierowca.autobus}')
        
        # Uzupełnij listę kierowców w listboxie. Jeśli jest załączony filtr to odfiltruj pasujących.
        for idx, aktualny_klient in enumerate(self.lista_klietnow):
            if not self.czy_filtr_jest_wlaczony.get() or aktualny_klient.autobus == aktualnie_wybarny_autobus_text:
                self.listbox_lista_klientow.insert(idx, f'{aktualny_klient.imie} {aktualny_klient.nazwisko}, '
                                                f'{aktualny_klient.lokalizacja}, {aktualny_klient.autobus}')
    

    # Funkcja odpowiedzialna za dodanie nowego autobusu do zakładu.
    def dodaj_autobus(self, wsp_xy = None):
        nowy_autobus = KlasaAutobus() # Wykreowanie nowego autobusu.

        # Jeśli zostały dostarczone współrzędne geograficzne to sprawdź jaka to lokalizacja i wpisz do nowego obiektu.
        if wsp_xy:
            nowa_lokalizacja = wspolrzedne_na_miejsce(wsp_xy)
            nowy_autobus.lokalizacja = nowa_lokalizacja

        # Otwórz okno uzupełnienia danych obiektu.
        nowy_autobus.okno_edycji_autobusu()
        # Po uzupełnieniu danych dodaj nowy autobus do taboru.
        self.lista_autobusow.append(nowy_autobus) if nowy_autobus.lokalizacja != "" and nowy_autobus.nazwa_autobusu != "" else ""
        # Po dodaniu nowego autobusu odśwież dane w oknie.
        self.uaktalnij_dane()


    # Funkcja do edycji istniejącego autobusu
    def edytuj_autobus(self):
        # Odszukaj co jest teraz zaznaczone.
        edytownay_autobus = self.listbox_lista_autobusow.get(ACTIVE)
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_autobus in self.lista_autobusow:
            if f'{aktualny_autobus.nazwa_autobusu} , {aktualny_autobus.lokalizacja}' == edytownay_autobus:
                # jeśli go znalazłeś to wyświetl okno edycji
                aktualny_autobus.okno_edycji_autobusu()
                # A potem wyjdź z pętli
                break
        # Na koniec odśwież widok.
        self.uaktalnij_dane()
    

    # Funkcja do usuwania autobusu
    def usun_autobus(self):
        # Odszukaj co jest teraz zaznaczone.
        edytownay_autobus = self.listbox_lista_autobusow.get(ACTIVE)
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_autobus in self.lista_autobusow:
            if f'{aktualny_autobus.nazwa_autobusu} , {aktualny_autobus.lokalizacja}' == edytownay_autobus:
                 # jeśli go znalazłeś to usuń go z listy autobusów
                self.lista_autobusow.remove(aktualny_autobus)
                # A potem wyjdź z pętli
                break
        # Na koniec odśwież widok.
        self.uaktalnij_dane()


    # Funkcja odpowiedzialna za dodanie nowego kierowcy.
    def dodaj_kierowce(self):
        nowy_kierowca = KlasaKierowca() # Wykreowanie nowego kierowcy.
        nowy_kierowca.okno_edycji_kierowcy(self.lista_autobusow)  # Otwórz okno uzupełnienia danych obiektu.
        # Po uzupełnieniu danych dodaj nowego kierowcę.
        self.lista_kierowcow.append(nowy_kierowca) if nowy_kierowca.lokalizacja != "" and nowy_kierowca.imie != "" else ""
        self.uaktalnij_dane() # Na koniec odśwież widok.


    # Funkcja do edycji istniejącego kierowcy
    def edytuj_kierowce(self):
        # Odszukaj co jest teraz zaznaczone.
        edytownay_kierowca = self.listbox_lista_kierowcow.get(ACTIVE)
        # Sprawdź który kierowca ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_kierowca in self.lista_kierowcow:
            if f'{aktualny_kierowca.imie} {aktualny_kierowca.nazwisko}, ' + \
               f'{aktualny_kierowca.lokalizacja}, {aktualny_kierowca.autobus}' == edytownay_kierowca:
                aktualny_kierowca.okno_edycji_kierowcy(self.lista_autobusow) # jeśli go znalazłeś to wyświetl okno edycji
                break # A potem wyjdź z pętli
        self.uaktalnij_dane() # Na koniec odśwież widok.
    

    # Funkcja do usuwania kierowcy.
    def usun_kierowce(self):
        # Odszukaj co jest teraz zaznaczone.
        edytownay_kierowca = self.listbox_lista_kierowcow.get(ACTIVE)
        # Sprawdź który kierowca ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_kierowca in self.lista_kierowcow:
            if f'{aktualny_kierowca.imie} {aktualny_kierowca.nazwisko}, ' + \
               f'{aktualny_kierowca.lokalizacja}, {aktualny_kierowca.autobus}' == edytownay_kierowca:
                self.lista_kierowcow.remove(aktualny_kierowca) # jeśli go znalazłeś to usuń go z listy kierowców
                break  # A potem wyjdź z pętli
        self.uaktalnij_dane() # Na koniec odśwież widok.
    
    
    # Funkcja odpowiedzialna za dodanie nowego klienta.
    def dodaj_klienta(self):
        nowy_klient = KlasaKlient() # Wykreowanie nowego klienta.
        nowy_klient.okno_edycji_klienta(self.lista_autobusow) # Otwórz okno uzupełnienia danych obiektu.
        # Po uzupełnieniu danych dodaj nowego klienta.
        self.lista_klietnow.append(nowy_klient) if nowy_klient.lokalizacja != "" and nowy_klient.imie != "" else ""
        self.uaktalnij_dane() # Na koniec odśwież widok.


    # Funkcja do edycji istniejącego klienta
    def edytuj_klienta(self):
        # Odszukaj co jest teraz zaznaczone.
        edytowany_klient = self.listbox_lista_klientow.get(ACTIVE)
        # Sprawdź który klient ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_klient in self.lista_klietnow:
            if f'{aktualny_klient.imie} {aktualny_klient.nazwisko}, ' + \
               f'{aktualny_klient.lokalizacja}, {aktualny_klient.autobus}' == edytowany_klient:
                aktualny_klient.okno_edycji_klienta(self.lista_autobusow) # jeśli go znalazłeś to wyświetl okno edycji
                break  # A potem wyjdź z pętli
        self.uaktalnij_dane() # Na koniec odśwież widok.
    

    # Funkcja do usuwania klienta.
    def usun_klienta(self):
        # Odszukaj co jest teraz zaznaczone.
        edytowany_klient = self.listbox_lista_klientow.get(ACTIVE)
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_klient in self.lista_klietnow:
            if f'{aktualny_klient.imie} {aktualny_klient.nazwisko}, ' + \
               f'{aktualny_klient.lokalizacja}, {aktualny_klient.autobus}' == edytowany_klient:
                self.lista_klietnow.remove(aktualny_klient) # jeśli go znalazłeś to usuń go z listy klientów
                break # A potem wyjdź z pętli
        self.uaktalnij_dane() # Na koniec odśwież widok.


    # Zadaniem funkcji jest wyświetlenie wszystkich autobusów na mapie.
    def pokaz_wszystkie_autobusy(self):
        self.map_widget.set_zoom(13) # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        # Przejdź po całej liście obiektów, wyciągnij x, y i dodaj do mapy 
        for aktualny_autobus in self.lista_autobusow:
            self.map_widget.set_position(aktualny_autobus.wsp_x, 
                                         aktualny_autobus.wsp_y,
                                         marker=True, 
                                         text=aktualny_autobus.nazwa_autobusu)


    # Zadaniem tej funkcji jest wyświetlenie na mapie zaznaczonego autobusu.
    def pokaz_wybrany_autobus(self):
        # Odszukaj co jest teraz zaznaczone.
        wybrany_autobus = self.listbox_lista_autobusow.get(ACTIVE)
        autobus_do_wyswietlenia = None # Zmienna do zapamiętania zaznaczonego autobusu
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_autobus in self.lista_autobusow:
            if f'{aktualny_autobus.nazwa_autobusu} , {aktualny_autobus.lokalizacja}' == wybrany_autobus:
                autobus_do_wyswietlenia = aktualny_autobus # Zapisz znaleziony obiekt
                break # Wyjdź z pętli

        self.map_widget.set_zoom(17) # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        # Ustaw znacznik na podstawie znalezionego obiektu
        self.map_widget.set_position(autobus_do_wyswietlenia.wsp_x, 
                                    autobus_do_wyswietlenia.wsp_y,
                                    marker=True, 
                                    text=autobus_do_wyswietlenia.nazwa_autobusu)


    # Zadaniem funkcji jest wyświetlenie wszystkich kierowców na mapie.
    def pokaz_wszystkich_kierowcow(self):
        self.map_widget.set_zoom(13) # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        aktualnie_wybarny_autobus_text = str(self.listbox_lista_autobusow.get(ACTIVE)).split(" , ")[0]
        # Przejdź po całej liście obiektów, wyciągnij x, y i dodaj do mapy
        for aktualny_kierowca in self.lista_kierowcow:
            if not self.czy_filtr_jest_wlaczony.get() or aktualny_kierowca.autobus == aktualnie_wybarny_autobus_text:
                self.map_widget.set_position(aktualny_kierowca.wsp_x, 
                                            aktualny_kierowca.wsp_y,
                                            marker=True, 
                                            text=f"{aktualny_kierowca.imie} {aktualny_kierowca.nazwisko}")


    # Zadaniem tej funkcji jest wyświetlenie na mapie zaznaczonego kierowcy.
    def pokaz_wybranego_kierowce(self):
        # Odszukaj co jest teraz zaznaczone.
        wybrany_kierowca = self.listbox_lista_kierowcow.get(ACTIVE)
        kierowca_do_wyswietlenia = None # Zmienna do zapamiętania zaznaczonego kierowcy
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_kierowca in self.lista_kierowcow:
            if f'{aktualny_kierowca.imie} {aktualny_kierowca.nazwisko}, ' + \
               f'{aktualny_kierowca.lokalizacja}, {aktualny_kierowca.autobus}' == wybrany_kierowca:
                kierowca_do_wyswietlenia = aktualny_kierowca # Zapisz znaleziony obiekt
                break # Wyjdź z pętli

        self.map_widget.set_zoom(17)  # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        # Ustaw znacznik na podstawie znalezionego obiektu
        self.map_widget.set_position(kierowca_do_wyswietlenia.wsp_x, 
                                    kierowca_do_wyswietlenia.wsp_y,
                                    marker=True, 
                                    text=f"{kierowca_do_wyswietlenia.imie} {kierowca_do_wyswietlenia.nazwisko}")
        

    # Zadaniem funkcji jest wyświetlenie wszystkich kientów na mapie.
    def pokaz_wszystkich_klientow(self):
        self.map_widget.set_zoom(13) # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        aktualnie_wybarny_autobus_text = str(self.listbox_lista_autobusow.get(ACTIVE)).split(" , ")[0]
        # Przejdź po całej liście obiektów, wyciągnij x, y i dodaj do mapy
        for aktualny_klinet in self.lista_klietnow:
            if not self.czy_filtr_jest_wlaczony.get() or aktualny_klinet.autobus == aktualnie_wybarny_autobus_text:
                self.map_widget.set_position(aktualny_klinet.wsp_x, 
                                            aktualny_klinet.wsp_y,
                                            marker=True, 
                                            text=f"{aktualny_klinet.imie} {aktualny_klinet.nazwisko}")


    # Zadaniem tej funkcji jest wyświetlenie na mapie zaznaczonego klienta.
    def pokaz_wybranego_klienta(self):
        # Odszukaj co jest teraz zaznaczone.
        wybrany_klient = self.listbox_lista_klientow.get(ACTIVE)
        klient_do_wyswietlenia = None # Zmienna do zapamiętania zaznaczonego klienta.
        # Sprawdź który autobus ma dane takie jak w zaznaczony obiekt w listBox
        for aktualny_klinet in self.lista_klietnow:
            if f'{aktualny_klinet.imie} {aktualny_klinet.nazwisko}, ' + \
               f'{aktualny_klinet.lokalizacja}, {aktualny_klinet.autobus}' == wybrany_klient:
                klient_do_wyswietlenia = aktualny_klinet # Zapisz znaleziony obiekt
                break # Wyjdź z pętli

        self.map_widget.set_zoom(17) # Ustaw zoom na mapie
        self.map_widget.delete_all_marker() # Usuń inne znaczki na mapie
        # Ustaw znacznik na podstawie znalezionego obiektu
        self.map_widget.set_position(klient_do_wyswietlenia.wsp_x, 
                                    klient_do_wyswietlenia.wsp_y,
                                    marker=True, 
                                    text=f"{klient_do_wyswietlenia.imie} {klient_do_wyswietlenia.nazwisko}")
                
    
    def wstepne_dane(self):
        nowy_autobus = KlasaAutobus()
        nowy_autobus.nazwa_autobusu = "400"
        nowy_autobus.lokalizacja = "Księdza Franciszka Marmo, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Księdza Franciszka Marmo, 05-230 Kobyłka")
        nowy_autobus.wsp_x = wspolrzedne[0]
        nowy_autobus.wsp_y = wspolrzedne[1]
        self.lista_autobusow.append(nowy_autobus)

        nowy_autobus = KlasaAutobus()
        nowy_autobus.nazwa_autobusu = "403"
        nowy_autobus.lokalizacja = "Napoleona 2A, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Napoleona 2A, 05-230 Kobyłka")
        nowy_autobus.wsp_x = wspolrzedne[0]
        nowy_autobus.wsp_y = wspolrzedne[1]
        self.lista_autobusow.append(nowy_autobus)

        nowy_autobus = KlasaAutobus()
        nowy_autobus.nazwa_autobusu = "404"
        nowy_autobus.lokalizacja = "Logistyczna 3, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Logistyczna 3, 05-230 Kobyłka")
        nowy_autobus.wsp_x = wspolrzedne[0]
        nowy_autobus.wsp_y = wspolrzedne[1]
        self.lista_autobusow.append(nowy_autobus)

        nowy_autobus = KlasaAutobus()
        nowy_autobus.nazwa_autobusu = "418"
        nowy_autobus.lokalizacja = "Karola Szymanowskiego, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Karola Szymanowskiego, 05-230 Kobyłka")
        nowy_autobus.wsp_x = wspolrzedne[0]
        nowy_autobus.wsp_y = wspolrzedne[1]
        self.lista_autobusow.append(nowy_autobus)

        nowy_autobus = KlasaAutobus()
        nowy_autobus.nazwa_autobusu = "500"
        nowy_autobus.lokalizacja = "Księdza Franciszka Marmo 31, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Księdza Franciszka Marmo 31, 05-230 Kobyłka")
        nowy_autobus.wsp_x = wspolrzedne[0]
        nowy_autobus.wsp_y = wspolrzedne[1]
        self.lista_autobusow.append(nowy_autobus)

        nowy_kierowca = KlasaKierowca()
        nowy_kierowca.imie = "Adam"
        nowy_kierowca.nazwisko = "Adamekowski"
        nowy_kierowca.autobus = "400"
        nowy_kierowca.lokalizacja = "Napoleona 2H, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Napoleona 2H, 05-230 Kobyłka")
        nowy_kierowca.wsp_x = wspolrzedne[0]
        nowy_kierowca.wsp_y = wspolrzedne[1]
        self.lista_kierowcow.append(nowy_kierowca)

        nowy_kierowca = KlasaKierowca()
        nowy_kierowca.imie = "Jola"
        nowy_kierowca.nazwisko = "Lojalna"
        nowy_kierowca.autobus = "403"
        nowy_kierowca.lokalizacja = "Nadarzyńska 67, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Nadarzyńska 67, 05-230 Kobyłka")
        nowy_kierowca.wsp_x = wspolrzedne[0]
        nowy_kierowca.wsp_y = wspolrzedne[1]
        self.lista_kierowcow.append(nowy_kierowca)

        nowy_kierowca = KlasaKierowca()
        nowy_kierowca.imie = "Bogdan"
        nowy_kierowca.nazwisko = "Boner"
        nowy_kierowca.autobus = "418"
        nowy_kierowca.lokalizacja = "Nadarzyn 8, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Nadarzyn 8, 05-230 Kobyłka")
        nowy_kierowca.wsp_x = wspolrzedne[0]
        nowy_kierowca.wsp_y = wspolrzedne[1]
        self.lista_kierowcow.append(nowy_kierowca)

        nowy_kierowca = KlasaKierowca()
        nowy_kierowca.imie = "Bogusław"
        nowy_kierowca.nazwisko = "Łęcina"
        nowy_kierowca.autobus = "500"
        nowy_kierowca.lokalizacja = "Krechowiecka 38, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Krechowiecka 38, 05-230 Kobyłka")
        nowy_kierowca.wsp_x = wspolrzedne[0]
        nowy_kierowca.wsp_y = wspolrzedne[1]
        self.lista_kierowcow.append(nowy_kierowca)

        nowy_kierowca = KlasaKierowca()
        nowy_kierowca.imie = "Tytus"
        nowy_kierowca.nazwisko = "Romek"
        nowy_kierowca.autobus = "500"
        nowy_kierowca.lokalizacja = "Pionierska 10, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Pionierska 10, 05-230 Kobyłka")
        nowy_kierowca.wsp_x = wspolrzedne[0]
        nowy_kierowca.wsp_y = wspolrzedne[1]
        self.lista_kierowcow.append(nowy_kierowca)

        nowy_klient = KlasaKlient()
        nowy_klient.imie = "Alicja"
        nowy_klient.nazwisko = "Czarow"
        nowy_klient.autobus = "400"
        nowy_klient.lokalizacja = "Napoleona 7, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Napoleona 7, 05-230 Kobyłka")
        nowy_klient.wsp_x = wspolrzedne[0]
        nowy_klient.wsp_y = wspolrzedne[1]
        self.lista_klietnow.append(nowy_klient)

        nowy_klient = KlasaKlient()
        nowy_klient.imie = "Miłosz"
        nowy_klient.nazwisko = "Mały"
        nowy_klient.autobus = "403"
        nowy_klient.lokalizacja = "Napoleona 2, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Napoleona 2, 05-230 Kobyłka")
        nowy_klient.wsp_x = wspolrzedne[0]
        nowy_klient.wsp_y = wspolrzedne[1]
        self.lista_klietnow.append(nowy_klient)

        nowy_klient = KlasaKlient()
        nowy_klient.imie = "Kazik"
        nowy_klient.nazwisko = "Barbarowicz"
        nowy_klient.autobus = "418"
        nowy_klient.lokalizacja = "Warszawska 2H, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Warszawska 2H, 05-230 Kobyłka")
        nowy_klient.wsp_x = wspolrzedne[0]
        nowy_klient.wsp_y = wspolrzedne[1]
        self.lista_klietnow.append(nowy_klient)

        nowy_klient = KlasaKlient()
        nowy_klient.imie = "Wiesiek"
        nowy_klient.nazwisko = "Puchacki"
        nowy_klient.autobus = "500"
        nowy_klient.lokalizacja = "Warszawska 44, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Warszawska 44, 05-230 Kobyłka")
        nowy_klient.wsp_x = wspolrzedne[0]
        nowy_klient.wsp_y = wspolrzedne[1]
        self.lista_klietnow.append(nowy_klient)

        nowy_klient = KlasaKlient()
        nowy_klient.imie = "Wojciech"
        nowy_klient.nazwisko = "Puczyk"
        nowy_klient.autobus = "500"
        nowy_klient.lokalizacja = "Królewska 15, 05-230 Kobyłka"
        wspolrzedne = miejsce_na_wspolrzedne("Królewska 15, 05-230 Kobyłka")
        nowy_klient.wsp_x = wspolrzedne[0]
        nowy_klient.wsp_y = wspolrzedne[1]
        self.lista_klietnow.append(nowy_klient)

        self.uaktalnij_dane()