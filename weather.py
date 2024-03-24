import requests
from config import OPENWEATHER_API_KEY
import os
from dataclasses import dataclass


api_key = os.getenv('OPENWEATHER_API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

@dataclass
class ForecastData:
    date: str
    main: str
    description: str
    icon: str
    temperature: int




def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp'))
    )

    return data

def get_five_day_forecast(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric&cnt=5').json()
    forecast_data = []
    for item in resp['list']:
        date = item['dt_txt']
        main = item['weather'][0]['main']
        description = item['weather'][0]['description']
        icon = item['weather'][0]['icon']
        temperature = int(item['main']['temp'])
        forecast_data.append(ForecastData(date=date, main=main, description=description, icon=icon, temperature=temperature))
    return forecast_data

def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    current_weather = get_current_weather(lat, lon, api_key)
    forecast = get_five_day_forecast(lat, lon, api_key)
    return current_weather, forecast

if __name__ == "__main__":
    city_name = 'Toronto'
    state_name = 'ON'
    country_name = 'Canada'
    current_weather, forecast = main(city_name, state_name, country_name)
    print("Current Weather:")
    print(current_weather)
    print("\nFive-Day Forecast:")
    for day in forecast:
        print(day)