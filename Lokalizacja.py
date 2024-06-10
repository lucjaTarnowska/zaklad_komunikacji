# Dany plik służy do zagregowania funkcji odpowiedzialnych za zamianę współrzędnych na adres i w drugą stronę
import ssl # Biblioteka do certyfikatów stron internetowych HTTPS.
import geopy
from geopy.geocoders import Nominatim # Biblioteka do odytywania o miejsca i współrzędne.

# Dany obiekt służy do stworzenia kontekstu SSL czyli zabezpieczeń witryn internetowych.
# W nowym kontekście wyłączamy sprawdzanie certyfikatów. Dany kontekst zostanie użyty do biblioteki Nominatim.
# Jest on niezbędny aby uniknąć błędów certyfikatu podczas odpytywania o adresy.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ustawienie agenta w nagłówku. Wymaga tego dana biblioteka.
geolocator = Nominatim(user_agent="Chrome/104.0.5112.79", ssl_context=ctx, adapter_factory=geopy.adapters.URLLibAdapter) 


def miejsce_na_wspolrzedne(miejsce):
    wspolrzedne = geolocator.geocode(miejsce, timeout=10)
    return wspolrzedne.latitude, wspolrzedne.longitude if wspolrzedne else 0, 0


def wspolrzedne_na_miejsce(wspolrzedne):
    miejsce = geolocator.reverse(wspolrzedne, timeout=10) 
    return miejsce.address if miejsce else "Miejsce blizej nieokreslone" 
