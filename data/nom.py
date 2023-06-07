from geopy.geocoders import Nominatim
import csv

def get_geolocation(block,address, zip_code):
    geolocator = Nominatim(user_agent="asdljasdnl1")
    location = geolocator.geocode(f"{block} {address}, {zip_code}")
    try:
        return (location.latitude, location.longitude)
    except:
        pass




