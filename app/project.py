import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Google Maps Distance and Time

import googlemaps
from datetime import datetime

now = datetime.now()

# gmaps_api_key = os.environ.get("gmaps_api_key")
# gmaps = googlemaps.Client(key=gmaps_api_key)
# 
# origin = input("Please enter the origin address: ")
# destination = input("Please enter the destination address: ")
# 
# while True:
#     preferred_transport = input("Please select your preferred transport: driving, bicycling, transit, walking: ")
#     if preferred_transport == "driving":
#         directions_route = preferred_transport
#         break
#     if preferred_transport == "bicycling":
#         directions_route = preferred_transport
#         break
#     if preferred_transport == "walking":
#         directions_route = preferred_transport
#         break
#     if preferred_transport == "transit":
#         directions_route = preferred_transport
#         break
#     elif preferred_transport != "driving" or "bicycling" or "walking" or "transit":
#         print("You entered an invalid preferred transport. Please try again: ")
# 
# directions_result = gmaps.directions(origin, destination, mode = directions_route, avoid = "ferries", departure_time=now)
# 
# while True:
#     if directions_route == "driving" or "bicycling" or "walking":
#         print("You are", directions_result[0]['legs'][0]['distance']['text'], "from your destination.")
#         print("Your commute time will be", directions_result[0]['legs'][0]['duration']['text'], ".")
#         break
#     if directions_route == "transit":
#         print("You are", directions_result[0]['legs'][0]['distance']['text'], "from your destination.")
#         print("Your commute time will be", directions_result[0]['legs'][0]['duration']['text'], ".")
#         print("You will arrive at", directions_result[0]['legs'][0]['arrival_time']['text'], ".") #NEED TO FIX. NOTHING APPEARS
#         break
#     else:
#         print("The travel mode was incorrectly entered. Please try again: ")


# WEATHER

# weather_api_key = os.environ.get("weather_api_key")
# 
# while True:
#     zip_code = input("Please enter a 5 digit .zip code for your weather report: ")
#     if not zip_code.isdigit():
#         print("Your .zip code contains non-numerical digits. Please try again: ")
#     if len(zip_code) >5:
#         print("Your .zip code contains too many digits. Please try again: ")
#     if len(zip_code) <5:
#         print("Your .zip code contains too few digits. Please try again: ")
#     if zip_code.isdigit() and len(zip_code) == 5:
#         break
# 
# def temp_format(temperatures):
#     return '{:,.2f}'.format(temperatures)
# 
# weather_url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + weather_api_key + "&q=" + zip_code
# forecast_response = requests.get(weather_url)
# response_key = forecast_response.json() # https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# if response_key["cod"] != "404":
#     main_key = response_key["main"]
#     current_temp = main_key["temp"]
#     kelvin2fahrenheit = (int(current_temp) - 273.15) * (9/5) + 32
#     weather_key = response_key["weather"]
#     describe_weather = weather_key[0]["description"]
#     print("The current temperature is " + str(temp_format(kelvin2fahrenheit)) + " degrees Fahrenheit" +
#     "\n and is " + str(describe_weather))
# else:
#     print(".zip code not found. Please try again: ")

# NEWS
from newsapi.newsapi_client import NewsApiClient
news_api_key = os.environ.get("news_api_key")

news_api_var = NewsApiClient(api_key=news_api_key)

nyt_news_stories = newsapi.get_top_headlines(sources='the-new-york-times')









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