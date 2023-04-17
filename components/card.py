from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from utils import tools

class Card(QWidget):
    def __init__(self, day, icon, temp):
        super().__init__()
        # self.day = day
        # self.icon = icon
        # self.temp = temp
        
        self.setStyleSheet('QLabel{background-color : grey;qproperty-alignment: AlignCenter;font-size: 20px;}')
        
        layout = QVBoxLayout()
        day_lbl = QLabel(day)
        icon_lbl = QLabel()
        icon_lbl.setPixmap(tools.getIcon(icon))
        icon_lbl.setScaledContents(True)
        
        temp_lbl = QLabel(temp)
        
        layout.addWidget(day_lbl)
        layout.addWidget(icon_lbl)
        layout.addWidget(temp_lbl)
        layout.setSpacing(0)
        
        self.setLayout(layout)
        
        