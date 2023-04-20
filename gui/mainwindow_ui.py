# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QWidget)
from . import resources_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1179, 748)
        palette = QPalette()
        brush = QBrush(QColor(0, 85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(13, 109, 160, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        mainwindow.setPalette(palette)
        mainwindow.setStyleSheet(u"\n"
"QWidget#mainwindow{\n"
"	\n"
"	background-color: rgba(13,109,160,255);\n"
"	color : white;\n"
"}\n"
"QLabel{\n"
"color : white;\n"
"}\n"
"\n"
"QLabel[accessibleName=\"h1\"]{\n"
"\n"
"	font-size :30px;\n"
"	font-weight : bold;\n"
"\n"
"\n"
"}\n"
"QLabel[accessibleName=\"h2\"]{\n"
"\n"
"	font-size :25px;\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel[accessibleName=\"h3\"]{\n"
"\n"
"	font-size :20px;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(mainwindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setContentsMargins(50, 50, 50, 50)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_4 = QLabel(mainwindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)

        self.sunset_lbl = QLabel(mainwindow)
        self.sunset_lbl.setObjectName(u"sunset_lbl")
        self.sunset_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.sunset_lbl, 4, 6, 1, 1)

        self.label_30 = QLabel(mainwindow)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_30, 5, 6, 1, 1)

        self.lowtemp_lbl = QLabel(mainwindow)
        self.lowtemp_lbl.setObjectName(u"lowtemp_lbl")
        self.lowtemp_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.lowtemp_lbl, 4, 4, 1, 1)

        self.date_lbl = QLabel(mainwindow)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.date_lbl, 1, 0, 1, 1)

        self.label_28 = QLabel(mainwindow)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_28, 3, 6, 1, 1)

        self.weatherdesc_lbl = QLabel(mainwindow)
        self.weatherdesc_lbl.setObjectName(u"weatherdesc_lbl")
        font = QFont()
        self.weatherdesc_lbl.setFont(font)
        self.weatherdesc_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.weatherdesc_lbl, 5, 1, 1, 2)

        self.label_26 = QLabel(mainwindow)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_26, 5, 5, 1, 1)

        self.maintemp_lbl = QLabel(mainwindow)
        self.maintemp_lbl.setObjectName(u"maintemp_lbl")
        font1 = QFont()
        font1.setPointSize(60)
        font1.setBold(True)
        self.maintemp_lbl.setFont(font1)
        self.maintemp_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.maintemp_lbl, 2, 1, 3, 2)

        self.mainweather_icon = QLabel(mainwindow)
        self.mainweather_icon.setObjectName(u"mainweather_icon")
        self.mainweather_icon.setScaledContents(True)
        self.mainweather_icon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mainweather_icon, 2, 0, 4, 1)

        self.highttemp_lbl = QLabel(mainwindow)
        self.highttemp_lbl.setObjectName(u"highttemp_lbl")
        self.highttemp_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.highttemp_lbl, 2, 4, 1, 1)

        self.humidity_lbl = QLabel(mainwindow)
        self.humidity_lbl.setObjectName(u"humidity_lbl")
        self.humidity_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.humidity_lbl, 4, 5, 1, 1)

        self.label_12 = QLabel(mainwindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_12, 5, 4, 1, 1)

        self.line = QFrame(mainwindow)
        self.line.setObjectName(u"line")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.line.setFont(font2)
        self.line.setStyleSheet(u"color: rgb(159, 159, 159);")
        self.line.setInputMethodHints(Qt.ImhNone)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 2, 3, 4, 1)

        self.sunrise_lbl = QLabel(mainwindow)
        self.sunrise_lbl.setObjectName(u"sunrise_lbl")
        self.sunrise_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.sunrise_lbl, 2, 6, 1, 1)

        self.label_24 = QLabel(mainwindow)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_24, 3, 5, 1, 1)

        self.windspeed_lbl = QLabel(mainwindow)
        self.windspeed_lbl.setObjectName(u"windspeed_lbl")
        self.windspeed_lbl.setFont(font)
        self.windspeed_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.windspeed_lbl, 2, 5, 1, 1)

        self.country_lbl = QLabel(mainwindow)
        self.country_lbl.setObjectName(u"country_lbl")
        self.country_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.country_lbl, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 3, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_2.setVerticalSpacing(30)
        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(0)
        self.cards_layout.setObjectName(u"cards_layout")
        self.cards_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.gridLayout_2.addLayout(self.cards_layout, 1, 0, 1, 6)

        self.label_5 = QLabel(mainwindow)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 5, 1, 1)

        self.nextday_lbl = QLabel(mainwindow)
        self.nextday_lbl.setObjectName(u"nextday_lbl")
        self.nextday_lbl.setMaximumSize(QSize(50, 50))
        self.nextday_lbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextday_lbl.setPixmap(QPixmap(u":/images/icons/next-icon.png"))
        self.nextday_lbl.setScaledContents(True)

        self.gridLayout_2.addWidget(self.nextday_lbl, 0, 4, 1, 1)

        self.label_3 = QLabel(mainwindow)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.previousday_lbl = QLabel(mainwindow)
        self.previousday_lbl.setObjectName(u"previousday_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousday_lbl.sizePolicy().hasHeightForWidth())
        self.previousday_lbl.setSizePolicy(sizePolicy)
        self.previousday_lbl.setMaximumSize(QSize(50, 50))
        self.previousday_lbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousday_lbl.setPixmap(QPixmap(u":/images/icons/previous-icon.png"))
        self.previousday_lbl.setScaledContents(True)

        self.gridLayout_2.addWidget(self.previousday_lbl, 0, 1, 1, 1)

        self.currentday_lbl = QLabel(mainwindow)
        self.currentday_lbl.setObjectName(u"currentday_lbl")
        font3 = QFont()
        font3.setPointSize(25)
        self.currentday_lbl.setFont(font3)
        self.currentday_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.currentday_lbl, 0, 2, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 2, 1)


        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"Weather", None))
#if QT_CONFIG(accessibility)
        self.label_4.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("mainwindow", u"hight", None))
#if QT_CONFIG(accessibility)
        self.sunset_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.sunset_lbl.setText(QCoreApplication.translate("mainwindow", u"21:23", None))
#if QT_CONFIG(accessibility)
        self.label_30.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_30.setText(QCoreApplication.translate("mainwindow", u"sunset", None))
#if QT_CONFIG(accessibility)
        self.lowtemp_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.lowtemp_lbl.setText(QCoreApplication.translate("mainwindow", u"18\u00b0", None))
#if QT_CONFIG(accessibility)
        self.date_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.date_lbl.setText(QCoreApplication.translate("mainwindow", u"Monday 12 April", None))
#if QT_CONFIG(accessibility)
        self.label_28.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_28.setText(QCoreApplication.translate("mainwindow", u"sunraise", None))
#if QT_CONFIG(accessibility)
        self.weatherdesc_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.weatherdesc_lbl.setText(QCoreApplication.translate("mainwindow", u"weather Desc", None))
#if QT_CONFIG(accessibility)
        self.label_26.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_26.setText(QCoreApplication.translate("mainwindow", u"Humidity", None))
#if QT_CONFIG(accessibility)
        self.maintemp_lbl.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.maintemp_lbl.setText(QCoreApplication.translate("mainwindow", u"21\u00b0", None))
        self.mainweather_icon.setText("")
#if QT_CONFIG(accessibility)
        self.highttemp_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.highttemp_lbl.setText(QCoreApplication.translate("mainwindow", u"23\u00b0", None))
#if QT_CONFIG(accessibility)
        self.humidity_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.humidity_lbl.setText(QCoreApplication.translate("mainwindow", u"0 %", None))
#if QT_CONFIG(accessibility)
        self.label_12.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("mainwindow", u"Low", None))
#if QT_CONFIG(accessibility)
        self.sunrise_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.sunrise_lbl.setText(QCoreApplication.translate("mainwindow", u"5:27", None))
#if QT_CONFIG(accessibility)
        self.label_24.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_24.setText(QCoreApplication.translate("mainwindow", u"wind", None))
#if QT_CONFIG(accessibility)
        self.windspeed_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.windspeed_lbl.setText(QCoreApplication.translate("mainwindow", u"7 MPH", None))
#if QT_CONFIG(accessibility)
        self.country_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h1", None))
#endif // QT_CONFIG(accessibility)
        self.country_lbl.setText(QCoreApplication.translate("mainwindow", u"London UK", None))
        self.label_5.setText("")
        self.nextday_lbl.setText("")
        self.label_3.setText("")
        self.previousday_lbl.setText("")
        self.currentday_lbl.setText(QCoreApplication.translate("mainwindow", u"Day TXT", None))
    # retranslateUi

