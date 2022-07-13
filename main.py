from unittest import result
import phonenumbers;
from mynumber import number;
from phonenumbers import geocoder;
from phonenumbers import carrier
import folium 
key="08ef28d81cf546daab482c2489b10943"
sanNumber=phonenumbers.parse(number)

yourLocation=geocoder.description_for_number(sanNumber,'en')

print(yourLocation)

service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)
query=str(yourLocation)


result=geocoder.geocode(query)
# print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to(mymap)
# save the map to a html file
mymap.save('myLocation.html')

