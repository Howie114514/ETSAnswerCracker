# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(351, 288)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"background-color: rgb(189, 167, 0);\n"
"              border-radius:5px;\n"
"              color:#fff;\n"
"              padding:2px;")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.eLabel = QLabel(Dialog)
        self.eLabel.setObjectName(u"eLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.eLabel)

        self.etsPathE = QLineEdit(Dialog)
        self.etsPathE.setObjectName(u"etsPathE")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.etsPathE)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.detectETSPathBtn = QPushButton(Dialog)
        self.detectETSPathBtn.setObjectName(u"detectETSPathBtn")

        self.horizontalLayout.addWidget(self.detectETSPathBtn)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.Label = QLabel(Dialog)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Label)

        self.answerDisplayTypeCB = QComboBox(Dialog)
        self.answerDisplayTypeCB.addItem("")
        self.answerDisplayTypeCB.addItem("")
        self.answerDisplayTypeCB.setObjectName(u"answerDisplayTypeCB")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.answerDisplayTypeCB)

        self.Label_3 = QLabel(Dialog)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Label_3)

        self.themeCB = QComboBox(Dialog)
        self.themeCB.addItem("")
        self.themeCB.addItem("")
        self.themeCB.setObjectName(u"themeCB")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.themeCB)


        self.verticalLayout.addLayout(self.formLayout)

        self.devOptions = QWidget(Dialog)
        self.devOptions.setObjectName(u"devOptions")
        self.verticalLayout_2 = QVBoxLayout(self.devOptions)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.devOptions)

        self.about = QPushButton(Dialog)
        self.about.setObjectName(u"about")

        self.verticalLayout.addWidget(self.about)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")

        self.verticalLayout.addWidget(self.save)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.verticalLayout.addWidget(self.cancel)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u8bbe\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Dialog", u"\u26a0\u8bf7\u8bbe\u7f6eE\u542c\u8bf4\u8def\u5f84\u4ee5\u63a2\u6d4b\u7b54\u6848\u8def\u5f84", None))
        self.eLabel.setText(QCoreApplication.translate("Dialog", u"e\u542c\u8bf4\u8def\u5f84", None))
        self.detectETSPathBtn.setText(QCoreApplication.translate("Dialog", u"\u68c0\u6d4b", None))
        self.Label.setText(QCoreApplication.translate("Dialog", u"\u7b54\u6848\u663e\u793a\u65b9\u5f0f", None))
        self.answerDisplayTypeCB.setItemText(0, QCoreApplication.translate("Dialog", u"\u6700\u77ed\u7b54\u6848", None))
        self.answerDisplayTypeCB.setItemText(1, QCoreApplication.translate("Dialog", u"\u5168\u90e8\u7b54\u6848", None))

        self.Label_3.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u9898", None))
        self.themeCB.setItemText(0, QCoreApplication.translate("Dialog", u"Light", None))
        self.themeCB.setItemText(1, QCoreApplication.translate("Dialog", u"Dark", None))

        self.about.setText(QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

