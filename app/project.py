# Import Packages and Modules

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
import googlemaps
from datetime import datetime

# Google Maps Distance and Time

now = datetime.now()

gmaps_api_key = os.environ.get("gmaps_api_key") #Google Maps API Key
gmaps = googlemaps.Client(key=gmaps_api_key)

origin = input("Please enter the origin address: ")
destination = input("Please enter the destination address: ")

while True: #https://developers.google.com/maps/documentation/directions/intro 
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
        print("You entered an invalid preferred transport. Please try again: ") #data validation

directions_result = gmaps.directions(origin, destination, mode = directions_route, 
avoid = "ferries", departure_time=now) #https://github.com/googlemaps/google-maps-services-python 

# WEATHER

weather_api_key = os.environ.get("weather_api_key") #OpenWeather API Key Retrieval

while True: #ZIP Code entry validation
    zip_code = input("Please enter a 5 digit ZIP code for your weather report: ")
    if not zip_code.isdigit():
        print("Your ZIP code contains non-numerical digits. Please try again: ")
    if len(zip_code) >5:
        print("Your ZIP code contains too many digits. Please try again: ")
    if len(zip_code) <5:
        print("Your ZIP code contains too few digits. Please try again: ")
    if zip_code.isdigit() and len(zip_code) == 5:
        break

def temp_format(temperatures): #format temperatures to 2 decimal places
    return '{:,.2f}'.format(temperatures)

weather_url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + weather_api_key + "&q=" + zip_code
forecast_response = requests.get(weather_url)
response_key = forecast_response.json() # https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

# NEWS

news_api_key = os.environ.get("news_api_key") #Obtain NewsAPI Key


#USER OUTPUTS

#Commute Times

print("\n")
print("\n")
print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Commute Information: ")
while True:
    if directions_route == "driving" or "bicycling" or "walking" or "transit": #print commute time and distance
        print("You are", directions_result[0]['legs'][0]['distance']['text'], "from your destination."
        " Your commute time will be", directions_result[0]['legs'][0]['duration']['text'],".")
        break
    else:
        print("The travel mode was incorrectly entered. Please try again: ")

#Weather

print("\n")
print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Today's weather forecast in your area: ")
if response_key["cod"] != "404": #https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
    main_key = response_key["main"]
    current_temp = main_key["temp"]
    kelvin2fahrenheit = (int(current_temp) - 273.15) * (9/5) + 32
    weather_key = response_key["weather"]
    describe_weather = weather_key[0]["description"]
    weather_output = print("The current temperature is " + str(temp_format(kelvin2fahrenheit)) + " degrees Fahrenheit" +
    " with " + str(describe_weather) + ".") #print temperature and weather conditions
else:
    print("ZIP code not found. Please try again: ")

#News
print("\n")
print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Today's news briefing from the New York Times: ")

def NYTNews(): 
    NYT_url = " https://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=" + news_api_key 
    #https://www.geeksforgeeks.org/fetching-top-news-using-news-api/
    NYT_page = requests.get(NYT_url).json()  
    all_articles = NYT_page["articles"] 
    top_news_titles = [] 
    top_news_descriptions = []
    top_news_urls = []
      
    for a in all_articles: #append empty lists with titles, descriptions, and URLs for day
        top_news_titles.append(a["title"])
        top_news_descriptions.append(a["description"]) 
        top_news_urls.append(a["url"])

    for k in range(len(top_news_titles)): #print user friendly briefing from NYT articles
        print(k+1,".", top_news_titles[k], "\n")
        print(top_news_descriptions[k], "\n") 
        print(top_news_urls[k], "\n", "\n")                 

if __name__ == '__main__': 
     NYTNews()  #invoke the function