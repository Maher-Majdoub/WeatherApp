from PySide6.QtWidgets import QApplication, QLabel, QLineEdit
from PySide6.QtGui import QPixmap, QColor
from components.mainwindow import MainWindow
#from utils.get_weather import getWeather
import urllib.request


if __name__ == '__main__':
    
    app = QApplication()
    window = MainWindow()
    window.show()
    
    
    app.exec()