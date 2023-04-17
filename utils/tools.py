from PySide6.QtGui import QPixmap
import os, requests
from .weather import Weather
from datetime import datetime


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
    
    w_info = response['weather'][0]
    w_main = response['main']
    weather = Weather(
        status = w_info['main'],
        description = w_info['description'],
        icon = w_info['icon'],
        temp = w_main['temp'],
        temp_min = w_main['temp_min'],
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
print(getCurrentDateTime())