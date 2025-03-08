from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from enum import Enum

import utils

class ToastTypes(Enum):
    Success=0
    Info=1
    Warning=2
    Error=3

ToastStyles = {
    ToastTypes.Info:"""border-bottom:3px solid blue""",
    ToastTypes.Success:"""border-bottom:3px solid #0e0;""",
    ToastTypes.Warning:"""border-bottom:3px solid #ee0;""",
    ToastTypes.Error:"""border-bottom:3px solid red;"""
}
    
toasts = []

class Toast(QDialog):
    def __init__(self, title,text,/,parent=None,type=ToastTypes.Success,duration=2):
        super().__init__(parent)
        toasts.append(self)
        self.titleLabel = QLabel(title,self)
        self.titleLabel.setStyleSheet("font-weight:600")
        self.titleLabel.setGeometry(6,0,200,15)
        self.textLabel = QLabel(text,self)
        self.textLabel.setGeometry(6,15,200,20)
        self.setStyleSheet("QDialog{color:#000;background-color:#fff;border:1px solid #ccc;margin-left:5px;"+ToastStyles[type]+"}")
        self.setGeometry(0,toasts.index(self)*45,0,40)
        anim = QPropertyAnimation(self,b"geometry",self)
        anim.setStartValue(self.geometry())
        anim.setDuration(300)
        g = self.geometry()
        anim.setEndValue(QRect(g.x(),toasts.index(self)*45,200,g.height()))
        anim.start()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show()
        timer = QTimer(self)
        timer.timeout.connect(lambda:utils.run(lambda:self.remove(),lambda:timer.stop()))
        timer.start(1000)
    
    def mouseDoubleClickEvent(self, event):
        self.remove()
        return super().mouseDoubleClickEvent(event)
    def update(self):
        anim = QPropertyAnimation(self,b"geometry",self)
        anim.setStartValue(self.geometry())
        anim.setDuration(100)
        g = self.geometry()
        anim.setEndValue(QRect(g.x(),toasts.index(self)*45,g.width(),g.height()))
        anim.start()
    def closeEvent(self, arg__1):
        toasts.pop(toasts.index(self))
        for t in toasts:
            t.update()
        return super().closeEvent(arg__1)
    def remove(self):
        if self.isHidden():
            return
        anim = QPropertyAnimation(self,b"size",self)
        anim.setStartValue(self.size())
        anim.setDuration(300)
        anim.setEndValue(QSize(1,40))
        anim.finished.connect(lambda:self.close())
        anim.start()

defaultWidget = None
def setDefaultWidget(d):
    global defaultWidget
    defaultWidget = d
def sendNotification(title,text,duration=2,/,parent=None,type=ToastTypes.Success,):
    global defaultWidget
    p = parent
    if p==None:
        p=defaultWidget
    return Toast(title,text,parent=p,type=type,duration=duration)