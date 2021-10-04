import phonenumbers
import folium
from test import number


from phonenumbers import geocoder
id_nmbr = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(id_nmbr, "id")
print(yourLocation)


from phonenumbers import carrier
service_nmbr = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmbr, "id"))

key = '7a6f156c14924a2b870993453e52aebe'

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
print(result)

# lat = result[0]['geometry']['lat']
# lng = result[0]['geometry']['lng']

# print(lat,lng)

# myMap = folium.Map(locatio=[lat,lng], zoom_start = 9)

# folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))


# myMap.save('location.html')
