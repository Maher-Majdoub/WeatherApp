from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from datetime import datetime
from utils import tools

class Card(QWidget):
    def __init__(self, weather : dict):
        super().__init__()
        # self.day = day
        # self.icon = icon
        # self.temp = temp
        
        self.setStyleSheet('QLabel{background-color : grey;qproperty-alignment: AlignCenter;font-size: 20px;}')
        
        layout = QVBoxLayout()
        time_lbl = QLabel(datetime.utcfromtimestamp(weather['dt']).strftime('%H:%M'))
        icon_lbl = QLabel()
        icon_lbl.setPixmap(tools.getIcon(weather['weather'][0]['icon']))
        icon_lbl.setScaledContents(True)
        
        temp_lbl = QLabel(str(round(weather['main']['temp'] - 273.15))+ '°C')
        
        layout.addWidget(time_lbl)
        layout.addWidget(icon_lbl)
        layout.addWidget(temp_lbl)
        layout.setSpacing(0)
        
        self.setLayout(layout)
        
        