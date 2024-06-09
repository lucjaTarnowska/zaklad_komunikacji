# Dany plik służy do zagregowania funkcji odpowiedzialnych za zamianę współrzędnych na adres i w drugą stronę

from geopy.geocoders import Nominatim # Biblioteka do odytywania o miejsca i współrzędne.

geolocator = Nominatim(user_agent="Mozilla/5.0") # Ustawienie agenta w nagłówku. Wymaga tego dana biblioteka.


def miejsce_na_wspolrzedne(miejsce):
    wspolrzedne = geolocator.geocode(miejsce, timeout=10)
    return wspolrzedne.latitude, wspolrzedne.longitude if wspolrzedne else 0, 0


def wspolrzedne_na_miejsce(wspolrzedne):
    miejsce = geolocator.reverse(wspolrzedne, timeout=10) 
    return miejsce.address if miejsce else "Miejsce blizej nieokreslone" 
