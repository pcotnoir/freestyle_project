
import json


#create map
# import gmaps
# gmaps.configure(api_key='AIzaSyDaWK8dgNvwiKcxL5RF8xefSlhmzx9XsEQ 	')
# 
# 
# with open('apikey.txt') as f:
#     api_key = f.readline()
#     f.close
# 
# gmaps = googlemaps.Client(key=api_key)
# 
# new_york_coordinates = (40.75, -74.00)
# gmaps.figure(center=new_york_coordinates, zoom_level=12)


# Google Maps Distance and Time

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDaWK8dgNvwiKcxL5RF8xefSlhmzx9XsEQ 	')


now = datetime.now()
directions_result = gmaps.directions("900 President Street Brooklyn, NY 11215",
                                     "750 Broadway New York, NY 10036",
                                     mode="transit",
                                     avoid="ferries",
                                     departure_time=now
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])


# {
#   origin: '936 President Street Brooklyn, NY 11215',
#   destination: '1500 Broadway New York, NY 10036',
#   travelMode: 'TRANSIT',
#   transitOptions: {
#    departureTime: new Date(1343641500),
#    modes: ['SUBWAY'],
#     routingPreference: 'FEWER_TRANSFERS'
#   },
#   unitSystem: google.maps.UnitSystem.IMPERIAL
# }

# from googlemaps import GoogleMaps
# 
# mapService = GoogleMaps()
# directions = mapService.directions('Houston', 'Atlanta')
# for step in directions['Directions']['Routes'][0]['Steps']:
#     print step['descriptionHtml']