from PySide6.QtWidgets import QWidget
from gui.mainwindow_ui import Ui_mainwindow
from .card import Card
from utils import tools
from utils.weather import Weather

class MainWindow(QWidget, Ui_mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.mainweather_icon.setPixmap(tools.getIcon('01d'))
                
        # card = Card("Today", '01d', '16°')
        # self.cards_layout.addWidget(card)
        # card = Card("Today", '01n', '16°')
        # self.cards_layout.addWidget(card)
        # card = Card("Today", '02d', '16°')
        # self.cards_layout.addWidget(card)
        # card = Card("Today", '01d', '16°')
        # self.cards_layout.setSpacing(0)
        # self.cards_layout.addWidget(card)
        self.setWeather()

    def setWeather(self):
        date_time = tools.getCurrentDateTime()

        coutry_name, country_code, global_weather, current_weather = tools.getWeather()
        print(current_weather)
        print(global_weather)
        weather = tools.convertToWeather(current_weather, current_weather['sys']['sunset'],  current_weather['sys']['sunset'])
        self.country_lbl.setText(f'{coutry_name},   {country_code}')
        self.mainweather_icon.setPixmap(tools.getIcon(weather.icon))

    
    