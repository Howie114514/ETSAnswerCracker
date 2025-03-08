# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agreement.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 193)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u514d\u8d23\u58f0\u660e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\n"
"              \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"              <html><head><meta name=\"qrichtext\" content=\"1\"\n"
"              /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"              p, li { white-space: pre-wrap; }\n"
"              hr { height: 1px; border-width: 0; }\n"
"              li.unchecked::marker { content: \"\\2610\"; }\n"
"              li.checked::marker { content: \"\\2612\"; }\n"
"              </style></head><body style=\" font-family:'Microsoft YaHei UI';\n"
"              font-size:9pt; font-weight:400; font-style:normal;\">\n"
"              <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
"              margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
"              font-weight:700;\">\u5b87\u5b99\u7ea7\u514d\u8d23\u58f0\u660e</span></p>\n"
"              <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
"              margin-right:0px; "
                        "-qt-block-indent:0;\n"
"              text-indent:0px;\">\u672c\u5de5\u5177\u662f\u7528\u4e8e\u7834\u89e3E\u542c\u8bf4\u7b54\u6848\u7684\u5de5\u5177\uff0c<span style=\"\n"
"              font-weight:700;\">\u5e76\u975e</span>\u7834\u89e3E\u5361\u7b49\u514d\u8d39\u53d6\u5f97E\u542c\u8bf4\u8f6f\u4ef6\u4f7f\u7528\u6743\u7684\u5de5\u5177\u3002\u4e0d\u4f1a\u6d89\u53ca\u8baf\u98de\u7684<span\n"
"              style=\"\n"
"              font-weight:700;\">\u4efb\u4f55</span>\u5229\u76ca\u3002\u53e6\u5916\uff0c\u542c\u8bf4\u9700\u8981\u957f\u65f6\u95f4\u7684\u7ec3\u4e60\uff0c\u8bf7\u8ba4\u6e05\u60a8\u7684\u81ea\u8eab\u6c34\u5e73\uff0c\u5c3d\u91cf<span\n"
"              style=\"\n"
"              font-weight:700;\">\u81ea\u5df1\u5b8c\u6210</span>\u542c\u8bf4\u4f5c\u4e1a\u3002\u8fc7\u5ea6\u4f9d\u8d56\u672c\u5de5\u5177\u5bfc\u81f4\u7684\u8003\u573a\u4e0a\u53d1\u6325\u5931\u5e38\u4f5c\u8005<span\n"
"              style=\"\n"
"              font-weight:700;\">\u6982\u4e0d\u8d1f\u8d23</span>\u3002</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u662f\u5426\u540c\u610f\uff1f", None))
    # retranslateUi

