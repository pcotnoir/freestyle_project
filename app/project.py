
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Google Maps Distance and Time

import googlemaps
from datetime import datetime

gmaps_api_key = os.environ.get("gmaps_api_key")
gmaps = googlemaps.Client(key=gmaps_api_key)

origin = input("Please enter the origin address: ")
destination = input("Please enter the destination address: ")
preferred_transport = input("Please select your preferred transport: driving, bicycling, transit, walking: ")

now = datetime.now()
directions_result = gmaps.directions(origin,
                                     destination,
                                     mode=preferred_transport,
                                     avoid="ferries",
                                     departure_time=now
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])
print(directions_result[0]['legs'][0]['arrival_time']['text'])


# import json, urllib, urllib.parse
# from urllib.parse import urlencode
# import googlemaps
# start = "Bridgewater, Sa, Australia"
# finish = "Stirling, SA, Australia"
# 
# url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
#             ('origin', start),
#             ('destination', finish)
#  ))
# ur = urllib.request.urlopen(url)
# result = json.load(ur)
# 
# for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
#     j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
#     print (j)


#create map
# import gmaps
# import googlemaps
# import pandas
# import os
# import gmaps.datasets
# gmaps.configure(api_key2= api_key)
#  
#  
# with open('apikey.txt') as f:
#      api_key = f.readline()
#      f.close
#  
# gmaps = googlemaps.Client(key='AIzaSyDaWK8dgNvwiKcxL5RF8xefSlhmzx9XsEQ 	')
#  
# new_york_coordinates = (40.75, -74.00)
# fig = gmaps.figure(center=new_york_coordinates, zoom_level=12)
# fig 