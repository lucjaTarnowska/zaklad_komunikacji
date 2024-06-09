# Dana klasa odpowiada za wyświetlanie strony logowania oraz to co ma się stać po poprawnym zalogowaniu się
from tkinter import * # Import biblioteki graficznej
from StronaMapy import * # import głównej strony aplikacji która ma się uruchomić po poprawnym zalogowaniu


class StronaLogowania:
    # Konstruktor klasy
    def __init__(self):

        # Słownik zawierający dozwolone loginy i hasła.
        self.baza_uzytkownikow = {
            "lucja": "blablabla",
            "marek": "pieczarek",
            "login": "pass"
        }

        # Widok okna
        self.root = Tk() # Utworzenie okna logowania.
        self.root.resizable(False, False) # Zablokowanie zmiany rozmiaru okna.
        self.root.title("Autobusy w Kobylce") # Tytuł na górej belce okna.
        self.root.geometry("420x200") # Rozmiar okna

        # Elementy na stronie logowania
        # Napisy
        napis_tytul_1 = Label(self.root, text="Aplikacja do zarzadzania autobusami w Kobylce")
        self.napis_jak_nie_wyjdzie_logowanie = Label(self.root, text="")
        napis_tytul_2 = Label(self.root, text="Dane logowania:")
        napis_login = Label(self.root, text="Login: ")
        napis_haslo = Label(self.root, text="Haslo: ")

        # Pola
        self.pole_login = Entry(self.root)
        self.pole_haslo = Entry(self.root, show="*")

        # Przyciski
        przycisk_do_logownia = Button(self.root, text="Zaloguj", width=17, command=self.logowanie_do_systemu)
        
        # Ustawienie położenia elementów na stronie
        napis_tytul_1.grid(row=0, column=0)
        self.napis_jak_nie_wyjdzie_logowanie.grid(row=1, column=0)
        napis_tytul_2.grid(row=2, column=0)
        napis_login.grid(row=3, column=0)
        napis_haslo.grid(row=4, column=0)
        self.pole_login.grid(row=3, column=1)
        self.pole_haslo.grid(row=4, column=1)
        przycisk_do_logownia.grid(row=5, column=1)

        self.root.mainloop() # Uruchomienie okna

    
    # Funkcja której zadaniem jest sprawdzenie wprowadzonych danych i jeżeli są poprawne to uruchomienie okna aplikacji.
    def logowanie_do_systemu(self):
        if self.pole_login.get() in self.baza_uzytkownikow: # Jeśli login jest w bazie 
            if self.baza_uzytkownikow[self.pole_login.get()] == self.pole_haslo.get(): # Oraz podane hasło zgadza się
                self.root.destroy() # To zamknij okno logowania
                StronaMapy() # I otwórz aplikację
            # Jesli dane były niepoprawne to wyświetl o tym komunikat.
            else:
                self.napis_jak_nie_wyjdzie_logowanie.config(text="Podane dane sa niepoprawne", fg='#f00')
        else:
            self.napis_jak_nie_wyjdzie_logowanie.config(text="Podane dane sa niepoprawne", fg='#f00')
        