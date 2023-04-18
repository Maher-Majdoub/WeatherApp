from PySide6.QtGui import QPixmap
import os, requests
from .weather import Weather
from datetime import datetime
import math

API_KEY = os.environ.get('openweathermap_APIKEY')
print(API_KEY)

def __getUserIP():
    # getting user-ip
    try:
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        if response:
            user_ip = response.json()['ip']
    except:
        # set up a default ip
        user_ip = '167.99.203.64'
        
    return user_ip
 
        
def __getLocation():
    USER_IP = __getUserIP()
    API_KEY = os.environ.get('apiip_APIKEY')
    try:
        url = f'http://apiip.net/api/check?ip={USER_IP}&accessKey={API_KEY}'
        response = requests.get(url).json()
        return response['countryName'], response['countryCode'], response['latitude'], response['longitude']
    except:
        print('wow')


def getWeather():
    loc = __getLocation()
    if loc:
        country_name, country_code, lat, lon = loc
    else :
        print('invalid location')
        return
    url1 = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response1 = requests.get(url1).json()
    response2 = requests.get(url2).json()
    return country_name, country_code, response1, response2


def getIcon(icon_id : str):
    file_path = os.path.join(os.path.dirname(__file__), '..', f'gui\\images\\weatherIcons\\{icon_id}.png')
    pixmap = QPixmap()
    pixmap.load(file_path)
    return pixmap

def convertToWeather(response : dict, sunset = 0, sunrise = 0):
    # this function create a Weather object from an api response  
    
    response = {'dt': 1682197200, 
                'main': {
                    'temp': 289.4, 
                    'feels_like': 288.57, 
                    'temp_min': 289.4, 
                    'temp_max': 289.4, 
                    'pressure': 1016, 
                    'sea_level': 1016, 
                    'grnd_level': 989, 
                    'humidity': 57, 
                    'temp_kf': 0}, 
                'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
                'clouds': {'all': 0}, 
                'wind': {'speed': 2.66, 'deg': 103, 'gust': 3.78}, 
                'visibility': 10000, 
                'pop': 0, 
                'sys': {'pod': 'n'}, 
                'dt_txt': '2023-04-22 21:00:00', 
                'city': {'id': 2473183, 'name': 'As Sanad', 'coord': {'lat': 34.4739, 'lon': 9.4613},
                         'country': 'TN', 'population': 7859, 'timezone': 3600, 'sunrise': 1681793243, 'sunset': 1681840522}}
    
    w_info = response['weather'][0]
    w_main = response['main']
    weather = Weather(
        status = w_info['main'],
        description = w_info['description'],
        icon = w_info['icon'],
        temp = round(w_main['temp']),
        temp_min = round(w_main['temp_min']),
        temp_max = w_main['temp_max'],
        wind_speed = response['wind']['speed'],
        dt = response['dt'],
        sunrise = sunrise,
        sunset = sunset
    )
    return weather
    

def getCurrentDateTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# weat = getWeather()
# for item in weat[2]['list']:
#     print(item)
#     print('#########################################')