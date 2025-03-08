# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        self.centralwidget.setFont(font1)
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
        self.status_lb.setStyleSheet(u"color:#fff;\n"
"background-color: rgb(0, 121, 14);")

        self.gridLayout.addWidget(self.status_lb, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"E\u542c\u8bf4\u5916\u6302", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7b54\u6848", None))
        self.copyBtn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.openFolderBtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939\u83b7\u53d6\u7b54\u6848", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/main/icon.ico\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">E\u542c\u8bf4\u5916\u6302</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\">v1.0.1 by <span style=\" font-weight:700;\">Howie</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Howie114514/EtsAnswerCracker\"><span style=\" text-decoration: underline; color:#003e92;\">\u5f00\u6e90\u5730\u5740 </span></a><a href=\"https://Howie114514.github.io/etsac\"><span style=\" text-decoration: underline; color:#003e92;\">\u5b98\u7f51</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#003e92;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u5f00\u59cb\u4f5c\u4e1a\u6216\u70b9\u51fb\u201c\u6253\u5f00\u6587\u4ef6\u5939\u83b7\u53d6\u7b54\u6848\u201d\u624b\u52a8"
                        "\u9009\u62e9\u8bb0\u5f55\u5373\u53ef\u83b7\u53d6\u7b54\u6848\u3002</span></p></body></html>", None))
        self.status_lb.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\uff1a\u672a\u542f\u52a8", None))
    # retranslateUi

