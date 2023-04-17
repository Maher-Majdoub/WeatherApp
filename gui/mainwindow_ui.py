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
    QLabel, QSizePolicy, QWidget)
from .images import resources_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(645, 557)
        mainwindow.setStyleSheet(u"QWidget#mainwindow{\n"
"	border-image: url(:/bg_image.jpg);\n"
"}\n"
"\n"
"QLabel[accessibleName=\"h1\"]{\n"
"	color : black;\n"
"	font-size :30px;\n"
"	font-weight : bold;\n"
"\n"
"\n"
"}\n"
"QLabel[accessibleName=\"h2\"]{\n"
"	color : black;\n"
"	font-size :25px;\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel[accessibleName=\"h3\"]{\n"
"	color : black;\n"
"	font-size :20px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(mainwindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(mainwindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)

        self.label_4 = QLabel(mainwindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)

        self.label_28 = QLabel(mainwindow)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_28, 3, 6, 1, 1)

        self.label_29 = QLabel(mainwindow)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_29, 4, 6, 1, 1)

        self.label_30 = QLabel(mainwindow)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_30, 5, 6, 1, 1)

        self.label_21 = QLabel(mainwindow)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 1)

        self.cards_layout = QHBoxLayout()
        self.cards_layout.setObjectName(u"cards_layout")

        self.gridLayout.addLayout(self.cards_layout, 7, 0, 3, 7)

        self.label_23 = QLabel(mainwindow)
        self.label_23.setObjectName(u"label_23")
        font = QFont()
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_23, 5, 1, 1, 2)

        self.label_22 = QLabel(mainwindow)
        self.label_22.setObjectName(u"label_22")
        font1 = QFont()
        font1.setPointSize(60)
        font1.setBold(True)
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 2, 1, 3, 2)

        self.mainweather_icon = QLabel(mainwindow)
        self.mainweather_icon.setObjectName(u"mainweather_icon")
        self.mainweather_icon.setScaledContents(True)
        self.mainweather_icon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mainweather_icon, 2, 0, 4, 1)

        self.label_3 = QLabel(mainwindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)

        self.label_26 = QLabel(mainwindow)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_26, 5, 5, 1, 1)

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

        self.label_12 = QLabel(mainwindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_12, 5, 4, 1, 1)

        self.label_25 = QLabel(mainwindow)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_25, 4, 5, 1, 1)

        self.label_27 = QLabel(mainwindow)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_27, 2, 6, 1, 1)

        self.label_15 = QLabel(mainwindow)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 1, 1, 1)

        self.label_16 = QLabel(mainwindow)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_16, 2, 5, 1, 1)

        self.label_24 = QLabel(mainwindow)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_24, 3, 5, 1, 1)

        self.label_31 = QLabel(mainwindow)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 6, 0, 1, 1)

        self.country_lbl = QLabel(mainwindow)
        self.country_lbl.setObjectName(u"country_lbl")
        self.country_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.country_lbl, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"Weather", None))
#if QT_CONFIG(accessibility)
        self.label_6.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_6.setText(QCoreApplication.translate("mainwindow", u"18\u00b0", None))
#if QT_CONFIG(accessibility)
        self.label_4.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("mainwindow", u"hight", None))
#if QT_CONFIG(accessibility)
        self.label_28.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_28.setText(QCoreApplication.translate("mainwindow", u"sunraise", None))
#if QT_CONFIG(accessibility)
        self.label_29.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_29.setText(QCoreApplication.translate("mainwindow", u"21:23", None))
#if QT_CONFIG(accessibility)
        self.label_30.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_30.setText(QCoreApplication.translate("mainwindow", u"sunset", None))
#if QT_CONFIG(accessibility)
        self.label_21.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_21.setText(QCoreApplication.translate("mainwindow", u"Monday 12 April", None))
#if QT_CONFIG(accessibility)
        self.label_23.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_23.setText(QCoreApplication.translate("mainwindow", u"weather Desc", None))
#if QT_CONFIG(accessibility)
        self.label_22.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_22.setText(QCoreApplication.translate("mainwindow", u"21\u00b0", None))
        self.mainweather_icon.setText("")
#if QT_CONFIG(accessibility)
        self.label_3.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("mainwindow", u"23\u00b0", None))
#if QT_CONFIG(accessibility)
        self.label_26.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_26.setText(QCoreApplication.translate("mainwindow", u"rain", None))
#if QT_CONFIG(accessibility)
        self.label_12.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("mainwindow", u"Low", None))
#if QT_CONFIG(accessibility)
        self.label_25.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_25.setText(QCoreApplication.translate("mainwindow", u"0 %", None))
#if QT_CONFIG(accessibility)
        self.label_27.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_27.setText(QCoreApplication.translate("mainwindow", u"5:27", None))
        self.label_15.setText(QCoreApplication.translate("mainwindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.label_16.setAccessibleName(QCoreApplication.translate("mainwindow", u"h2", None))
#endif // QT_CONFIG(accessibility)
        self.label_16.setText(QCoreApplication.translate("mainwindow", u"7 MPH", None))
#if QT_CONFIG(accessibility)
        self.label_24.setAccessibleName(QCoreApplication.translate("mainwindow", u"h3", None))
#endif // QT_CONFIG(accessibility)
        self.label_24.setText(QCoreApplication.translate("mainwindow", u"wind", None))
        self.label_31.setText(QCoreApplication.translate("mainwindow", u"todays weather", None))
#if QT_CONFIG(accessibility)
        self.country_lbl.setAccessibleName(QCoreApplication.translate("mainwindow", u"h1", None))
#endif // QT_CONFIG(accessibility)
        self.country_lbl.setText(QCoreApplication.translate("mainwindow", u"London UK", None))
    # retranslateUi

