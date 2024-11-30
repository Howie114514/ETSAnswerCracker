# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        icon = QIcon()
        icon.addFile(u":/main/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"        background-color:#fff\n"
"        }\n"
"        #centralwidget QTextBrowser{\n"
"        background-color:#fff;\n"
"        border:1px solid #ccc;\n"
"        border-radius:5px\n"
"        }\n"
"        #centralwidget QPushButton{\n"
"        background-color: rgb(0, 208, 24);\n"
"        border:0px;\n"
"        border-radius:5px;\n"
"        color:#fff;\n"
"        padding:3px;\n"
"        }\n"
"        #centralwidget QPushButton::hover{\n"
"        background-color: rgb(0, 100, 10);\n"
"        }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copyBtn = QPushButton(self.centralwidget)
        self.copyBtn.setObjectName(u"copyBtn")

        self.horizontalLayout.addWidget(self.copyBtn)

        self.exportBtn = QPushButton(self.centralwidget)
        self.exportBtn.setObjectName(u"exportBtn")

        self.horizontalLayout.addWidget(self.exportBtn)

        self.openFolderBtn = QPushButton(self.centralwidget)
        self.openFolderBtn.setObjectName(u"openFolderBtn")

        self.horizontalLayout.addWidget(self.openFolderBtn)

        self.settingsBtn = QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName(u"settingsBtn")

        self.horizontalLayout.addWidget(self.settingsBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QMainWindow{\n"
"                background-color:#fff\n"
"                }")

        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.status_lb = QLabel(self.centralwidget)
        self.status_lb.setObjectName(u"status_lb")
        self.status_lb.setStyleSheet(u"/*background-color: rgb(19, 194, 0);*/\n"
"                color:#fff;\n"
"                border-radius:5px;\n"
"                background-color: rgb(0, 121, 14);")

        self.gridLayout.addWidget(self.status_lb, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ETS\u5916\u6302", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7b54\u6848", None))
        self.copyBtn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.openFolderBtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939\u83b7\u53d6\u7b54\u6848", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.status_lb.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\uff1a\u672a\u542f\u52a8", None))
    # retranslateUi

