from geopy.geocoders import Nominatim
import csv

def get_geolocation(address, zip_code):
    geolocator = Nominatim(user_agent="angusdingly")
    location = geolocator.geocode(f"{address}, {zip_code}")
    return (location.latitude, location.longitude)

with open('data/crimedata.csv', 'r') as f:
    csvReader = csv.reader(f)

    for i in csvReader:
        print(i)
