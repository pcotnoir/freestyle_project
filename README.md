# "Freestyle Project" 
A freestyle project that serves as a morning flash briefing app. Issues requests to [Google Maps API](https://developers.google.com/maps/documentation/directions/intro) to provide commute times and distances, to [OpenWeather API](https://openweathermap.org/api) to provide current temperatures and weather conditions, and to [News API](https://newsapi.org/docs/get-started) to provide the top news headlines, intros to articles, and New York Times hyperlinks. 

## Prerequisites

+ Anaconda 3.7
+ Python 3.7
+ Pip

## Installation

Fork this repository under your own control and clone to your local desktop. Navigate to the program from GitBash:

```sh
cd freestyle_project
```

Use Anaconda to create and activate a new virtual environment: "freestyleproject-env":

```sh
conda create -n freestyleproject-env python=3.7 # first time only
conda activate freestyleproject-env
```

From inside the virtual environment, install the following packages:

```sh
pip install -r requirements.txt
pip install -U googlemaps
pip install newsapi-python
```

## Setup

Before developing the application, obtain unique API Keys for [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key), [OpenWeather](https://openweathermap.org/appid), and [News API](https://newsapi.org/docs/get-started). 

After obtaining the three unique API keys, create a new environment in Virtual Editor called ".env" and update the the .env file with your API keys. For example:

```sh
gmaps_api_key = "abc123"
weather_api_key = "def456"
news_api_key = "ghi789" 
```

Ensure that your .gitignore file in Virtual Editor also contains ".env" so that your unique API keys can be securely protected. 

## Usage

Run the script:

```py
python app/project.py
```

## [License](/LICENSE)

## Credits
Adopted from: [Professor Rossetti](https://github.com/prof-rossetti/robo-advisor-demo-2019/blob/master/README.md)