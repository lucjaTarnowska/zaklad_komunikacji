from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/5.0")


def miejsce_na_wspolrzedne(miejsce):
    wspolrzedne = geolocator.geocode(miejsce, timeout=10)
    return wspolrzedne.latitude, wspolrzedne.longitude
