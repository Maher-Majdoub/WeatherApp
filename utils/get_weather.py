import requests, os
from detect_location import getLocation
API_KEY = os.environ.get('openweathermap_APIKEY')

def getWeather():
    lat ,lon = getLocation()
    print(lat, lon)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url).json()
    
    print(response)
    
    
getWeather()