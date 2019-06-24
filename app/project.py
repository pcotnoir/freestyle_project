import json
import os
from dotenv import load_dotenv
load_dotenv()

# Google Maps Distance and Time

import googlemaps
from datetime import datetime

now = datetime.now()

gmaps_api_key = os.environ.get("gmaps_api_key")
gmaps = googlemaps.Client(key=gmaps_api_key)

origin = input("Please enter the origin address: ")
destination = input("Please enter the destination address: ")

while True:
    preferred_transport = input("Please select your preferred transport: driving, bicycling, transit, walking: ")
    if preferred_transport == "driving":
        directions_route = preferred_transport
        break
    if preferred_transport == "bicycling":
        directions_route = preferred_transport
        break
    if preferred_transport == "walking":
        directions_route = preferred_transport
        break
    if preferred_transport == "transit":
        directions_route = preferred_transport
        break
    elif preferred_transport != "driving" or "bicycling" or "walking" or "transit":
        print("You entered an invalid preferred transport. Please try again: ")

directions_result = gmaps.directions(origin, destination, mode = directions_route, avoid = "ferries", departure_time=now)

while True:
    if directions_route == "driving" or "bicycling" or "walking":
        print("You are", directions_result[0]['legs'][0]['distance']['text'], "from your destination.")
        print("Your commute time will be", directions_result[0]['legs'][0]['duration']['text'], ".")
        break
    if directions_route == "transit":
        print("You are", directions_result[0]['legs'][0]['distance']['text'], "from your destination.")
        print("Your commute time will be", directions_result[0]['legs'][0]['duration']['text'], ".")
        print("You will arrive at", directions_result[0]['legs'][0]['arrival_time']['text'], ".") #NEED TO FIX. NOTHING APPEARS
        break
    else:
        print("The travel mode was incorrectly entered. Please try again: ")


# WEATHER

weather_api_key = os.environ.get("weather_api_key")

# NEWS

news_api_key = os.environ.get("news_api_key")



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