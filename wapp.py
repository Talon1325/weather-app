#Basic weather app using console
import requests
import os
from dotenv import load_dotenv

# Use envirnoment file to hide your api_key
load_dotenv()
api_key = str(os.getenv('API_KEY'))

city = input("City: ")
#state_code = input("(Optional US) State Code:")
#country_code = input("(Optional) Country Code:")
#limit = input("(Optional) Limit:")

# Checks if city that is available and internet connection
try: 
    # API call to Geocoding API to find the lat and lon coordiates to the city
    city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
    # Send GET request to Open Weather App and convert unstructured data to a json format
    coords = requests.get(city_url).json()
    lat, lon = coords[0]['lat'], coords[0]['lon']

    # API call to Current Weather Data to find weather and temperature
    coord_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    weather_data = requests.get(coord_url).json()

    # Search for temperature and weather description and Convert temperature from kelvin to farenheit
    temp_farenheit = round((weather_data['main']['temp'] - 273.15) * 9/5 + 32)
    feelslike_farenheit = round((weather_data['main']['feels_like']- 273.15) * 9/5 + 32)
    weather = weather_data['weather'][0]['description']


    print('Temperature: ', temp_farenheit)
    print('Feels Like: ', feelslike_farenheit)
    print('Weather: ', weather)

except:
    print("City not found")

