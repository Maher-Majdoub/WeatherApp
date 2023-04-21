from PySide6.QtGui import QPixmap
from .weather import Weather
from datetime import datetime
import os, requests, yaml


API_KEY = os.environ.get('openweathermap_APIKEY')


def __getUserIP():
    # getting user-ip
    try:
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        user_ip = response.json()['ip']
    except:
        # set up a default ip
        user_ip = None
        
    return user_ip
     
def __getLocation():
    USER_IP = __getUserIP()
    if USER_IP : 
        try:
            API_KEY = os.environ.get('apiip_APIKEY')
            url = f'http://apiip.net/api/check?ip={USER_IP}&accessKey={API_KEY}'
            response = requests.get(url).json()
            return response['countryName'], response['countryCode'], response['latitude'], response['longitude']
        except:
            return None

def __getLocFromConfig():
    try:
        file_path =  os.path.join(os.path.dirname(__file__), '..', 'config.yml')
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
            
        loc = config['location']
        return loc['country_name'], loc['country_code'], loc['lat'], loc['lon']
    except:
        return None
def __getLocManualy():
    # not finished
    return 'London', 'UK', 51.507351, -0.127758
    
def __saveConfig(location, weather, forecast):
    file_path =  os.path.join(os.path.dirname(__file__), '..', 'config.yml')

    config = {
        'last-update' : datetime.now().strftime('%d/%m/%Y'),
        'location' : { 
            'country_name' : location[0],
            'country_code' : location[1],
            'lat' : location[2],
            'lon' : location[3]
            },
        'weather' : weather,
        'forecast' : forecast       
    }
    
    with open(file_path, 'w') as f:
        yaml.safe_dump(config, f)
        
def getWeatherFromConfig():
    file_path =  os.path.join(os.path.dirname(__file__), '..', 'config.yml')
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    if config['last-update'] == datetime.now().strftime('%d/%m/%Y'):  # updated today
        return config['forecast'], config['weather']
    
def getWeather():
    loc = __getLocation()
    if not loc:
        loc = __getLocFromConfig()
    
    if not loc:
        loc = __getLocManualy()

    country_name, country_code, lat, lon = loc
    try:
        url1 = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
        url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
        forecast = requests.get(url1).json()
        weather = requests.get(url2).json() 
        __saveConfig(loc, weather, forecast)
    except:
        saved = getWeatherFromConfig()
        if saved:
            forecast, weather = saved
        else:
            return None
    
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


