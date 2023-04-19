from PySide6.QtWidgets import QWidget
from gui.mainwindow_ui import Ui_mainwindow
from .card import Card
from utils import tools
from utils.weather import Weather
from datetime import datetime

class MainWindow(QWidget, Ui_mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.coutry_name, self.country_code, self.forecast, self.weather = tools.getWeather()
        
        print(self.forecast, '\n#######################', self.weather)

        forecast_list = [self.forecast['list'][i] for i in range(int(self.forecast['cnt']))]
        day1 = [forecast_list[i] for i in range(8)]
        day2 = [forecast_list[i] for i in range(8, 16)]
        day3 = [forecast_list[i] for i in range(16, 24)]
        day4 = [forecast_list[i] for i in range(24, 32)]
        day5 = [forecast_list[i] for i in range(32, 40)]
        del(forecast_list)

        self.mainweather_icon.setPixmap(tools.getIcon('01d'))
                
        card = Card(day1[0])
        self.cards_layout.addWidget(card)
        card = Card(day1[1])
        self.cards_layout.addWidget(card)
        card = Card(day1[2])
        self.cards_layout.addWidget(card)
        card = Card(day1[3])
        self.cards_layout.addWidget(card)
        card = Card(day1[4])
        self.cards_layout.addWidget(card)
        card = Card(day1[5])
        self.cards_layout.addWidget(card)
        card = Card(day1[6])
        self.cards_layout.addWidget(card)
        card = Card(day1[7])
        self.cards_layout.addWidget(card)

        self.setGlobalWeather()

    def setGlobalWeather(self):
        # coutry_name, country_code, global_weather, current_weather = tools.getWeather()
        # print(current_weather)
        # print(global_weather)
        weather = tools.convertWeather(self.weather)  # current_weather, current_weather['sys']['sunset'],  current_weather['sys']['sunset']
        sunrise = datetime.utcfromtimestamp(weather.sunrise).strftime('%H:%M')
        sunset = datetime.utcfromtimestamp(weather.sunset).strftime('%H:%M')
        self.country_lbl.setText(f'{self.coutry_name},  {self.country_code}')
        self.date_lbl.setText(tools.getCurrentDateTime())
        self.mainweather_icon.setPixmap(tools.getIcon(weather.icon))
        self.maintemp_lbl.setText(f'{round(weather.temp - 273.15)}°C')
        self.weatherdesc_lbl.setText(weather.description.title())
        self.highttemp_lbl.setText(f'{round(weather.temp_max - 273.15)}°C')
        self.lowtemp_lbl.setText(f'{round(weather.temp_min - 273.15)}°C')
        self.windspeed_lbl.setText(f'{round(weather.wind_speed)} mph')
        self.humidity_lbl.setText(f'{weather.humidity} %')
        self.sunrise_lbl.setText(sunrise)
        self.sunset_lbl.setText(sunset)


    def getAllDayWeather(self):
        pass
    
    