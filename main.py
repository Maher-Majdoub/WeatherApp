from PySide6.QtWidgets import QApplication
from components.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(app)
    try:
        window.show()
        app.exec()
    except:
        app.exit()
    