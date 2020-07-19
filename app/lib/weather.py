import os
import requests

URL = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.environ['WEATHER_API_KEY']


def fetch_weather(**location):
    lat = location['lat']
    lon = location['lon']
    exclude = 'current'  # 現在の気象情報は不要
    units = 'metric'  # 温度の単位をCelsiusにする
    params = {'lat': lat, 'lon': lon, 'exclude': exclude, 'units': units, 'appid': API_KEY}
    response = requests.get(URL, params=params)
    return response.json()

