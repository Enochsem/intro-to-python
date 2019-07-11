from geopy.geocoders import Nominatim
country1=str(input("enter your current country "))
country2=str(input("enter the search country "))
geolocator = Nominatim(user_agent="ENOCH'S DISTANCEBOT")

location = geolocator.geocode(country1)
print(location.address)
print((location.latitude, location.longitude))

location2 = geolocator.geocode(country2)
print(location2.address)
print((location2.latitude, location2.longitude))

from geopy.distance import geodesic
country1 = (location.latitude, location.longitude)
country2 = (location2.latitude, location2.longitude)
print("the distance is "+str(geodesic(country1,country2).miles))