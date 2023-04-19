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
    loc = ('Tunis', 'TN', 34.4739, 9.4613)   #__getLocation()
    if loc:
        country_name, country_code, lat, lon = loc
    else :
        print('invalid location')
        return
    url1 = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    forecast = eval(open((os.path.join(os.path.dirname(__file__), 'forecast.txt')), 'r').read()) #requests.get(url1).json()
    weather = eval(open((os.path.join(os.path.dirname(__file__), 'weather.txt')), 'r').read()) #requests.get(url2).json()
    return country_name, country_code, forecast, weather


def getIcon(icon_id : str):
    file_path = os.path.join(os.path.dirname(__file__), '..', f'gui\\images\\weatherIcons\\{icon_id}.png')
    pixmap = QPixmap()
    pixmap.load(file_path)
    return pixmap

def convertWeather(response : dict):
    # this function create a Weather object from an api response  
    
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
        humidity = w_main['humidity'],
        sunrise = response['sys']['sunrise'],
        sunset = response['sys']['sunset']
    )
    return weather

def convertForecast(forecast : dict):
    pass

def getCurrentDateTime():
    return datetime.now().strftime("%A %d %B")

# weat = getWeather()
# for item in weat[2]['list']:
#     print(item)
#     print('#########################################')