from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from gui.mainwindow_ui import Ui_mainwindow
from .card import Card
from utils import tools
from datetime import datetime

class MainWindow(QWidget, Ui_mainwindow):
    def __init__(self, app : QApplication):
        w = tools.getWeather()
        super().__init__()
        if w:
            self.setupUi(self)
            self.gridLayout.setContentsMargins(10, 10, 10, 10)
            self.currentShowedDay = 1
            self.coutry_name, self.country_code, self.forecast, self.weather = w
            forecast_list = [self.forecast['list'][i] for i in range(int(self.forecast['cnt']))]
            day1 = [forecast_list[i] for i in range(8)]
            day2 = [forecast_list[i] for i in range(8, 16)]
            day3 = [forecast_list[i] for i in range(16, 24)]
            day4 = [forecast_list[i] for i in range(24, 32)]
            day5 = [forecast_list[i] for i in range(32, 40)]
            del(forecast_list)
            self.days = [day1, day2, day3, day4, day5]
            self.setGlobalWeather()
            self.previousday_lbl.mousePressEvent = self.showPreviousDay
            self.nextday_lbl.mousePressEvent = self.showNextDay
        else: 
            QMessageBox.warning(self, 'No Internet Connection', 'Please check the internet connection and rerun the application !')
            raise Exception('No Internet')

        

    def setGlobalWeather(self):
        weather = tools.convertWeather(self.weather) 
        sunrise = datetime.utcfromtimestamp(weather.sunrise).strftime('%H:%M')
        sunset = datetime.utcfromtimestamp(weather.sunset).strftime('%H:%M')
        self.country_lbl.setText(f'{self.coutry_name},  {self.country_code}')
        self.date_lbl.setText(datetime.utcfromtimestamp(weather.dt).strftime('%A %d %B'))
        self.mainweather_icon.setPixmap(tools.getIcon(weather.icon))
        self.maintemp_lbl.setText(f'{round(weather.temp - 273.15)}°C')
        self.weatherdesc_lbl.setText(weather.description.title())
        self.highttemp_lbl.setText(f'{round(weather.temp_max - 273.15)}°C')
        self.lowtemp_lbl.setText(f'{round(weather.temp_min - 273.15)}°C')
        self.windspeed_lbl.setText(f'{round(weather.wind_speed)} mph')
        self.humidity_lbl.setText(f'{weather.humidity} %')
        self.sunrise_lbl.setText(sunrise)
        self.sunset_lbl.setText(sunset)
        
        self.loadDay(self.days[0])
        self.currentShowedDay = 1
        self.previousday_lbl.setEnabled(False)
        


    def getAllDayWeather(self):
        pass
    
    def showPreviousDay(self, x = None):
        self.nextday_lbl.setEnabled(True)
        if self.currentShowedDay > 1:
            self.loadDay(self.days[self.currentShowedDay-2])
            self.currentShowedDay -= 1
            
        if self.currentShowedDay <= 1:
            self.previousday_lbl.setEnabled(False)
        
        
    def showNextDay(self, x = None):
        self.previousday_lbl.setEnabled(True)
        if self.currentShowedDay < len(self.days):
            self.loadDay(self.days[self.currentShowedDay])
            self.currentShowedDay += 1
        
        if self.currentShowedDay >= len(self.days):
            self.nextday_lbl.setEnabled(False)
        
    def loadDay(self, day):
        for i in reversed(range(self.cards_layout.count())):
            widget = self.cards_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
                # remove the widget from memory
                self.cards_layout.removeWidget(widget)
                widget.deleteLater()

        for d in day:
            card = Card(d)
            self.cards_layout.addWidget(card)
        
        self.currentday_lbl.setText(datetime.utcfromtimestamp(day[0]['dt']).strftime('%a %d %b'))
        