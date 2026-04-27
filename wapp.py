#Basic weather app using console
import sys
import requests

api_key = 'e489d2a9660760f0ee11d3178a4f9dce'
city = input("City: ")
#state_code = input("(Optional US) State Code:")
#country_code = input("(Optional) Country Code:")
#limit = input("(Optional) Limit:")
try: 
    city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
    coords = requests.get(city_url)
    lat, lon = coords.json()[0]['lat'], coords.json()[0]['lon']
    coord_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    weather_data = requests.get(coord_url).json()
    temp_farenheit = round((weather_data['main']['temp'] - 273.15) * 9/5 + 32)
    feelslike_farenheit = round((weather_data['main']['feels_like']- 273.15) * 9/5 + 32)
    weather = weather_data['weather'][0]['description']
    print('Temperature: ', temp_farenheit)
    print('Feels Like: ', feelslike_farenheit)
    print('Weather: ', weather)
except:
    print("City not found")

