import os
import threading
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main_ui import Ui_MainWindow
import utils
import constants
import settings_ui
import about_ui
import agreement_ui
import json
from settings import settings
import re

def generateAnswers(dir):
    folders = os.listdir(dir)
    contents = []
    templates = []
    for d in folders:
        p = os.path.join(dir,d)
        if re.match("content_.*",d):
            print("[content]",d)
            contents.append(p)
        else:
            templates.append(p)
    print(contents,templates)
    res = ""
    num=1
    for c in contents:
        print(c)
        
        content = json.load(open(os.path.join(c,"content.json"),encoding="utf-8"))
        if content["structure_type"]=="collector.read":
            print("模仿朗读：",c)
            res+="<h2>"+str(num)+"：模仿朗读</h2>"
            res+=content["info"]["value"]
            res+="<br>"
        elif content["structure_type"]=="collector.picture":
            print("复述：",c)
            res+="<h2>"+str(num)+"：</h2>"
            std = content["info"]["std"]
            answer = ""
            for a in std:
                if settings.read(int,"ets","mode",0)==1:
                    answer+=a["value"]+"<br>"
                else:
                    if len(a["value"])<len(answer):
                        answer=a["value"]
                    elif answer=="":
                        answer=a["value"]
            res+=answer
            res+="<br>"
        else:
            print("一般题目：",c)
            res+="<h2>"+str(num)+"：</h2>"
            n=1
            for q in content["info"]["question"]:
                res+="("+str(n)+") "
                std = q["std"]
                answer = ""
                for a in std:
                    if settings.read(int,"ets","mode",0)==1:
                        answer+=a["value"]+"<br>"
                    else:
                        if len(a["value"])<len(answer):
                            answer=a["value"]
                        elif answer=="":
                            answer=a["value"]
                res+=answer
                n+=1
                res+="<br>"
            res+="<br>"
        num+=1
    return res

def closeDialog(d):
    mwui.centralwidget.setDisabled(False)
    d.close()

def agreeAgreement():
    settings.set("agreement","agreed","true")
    settings.saveConfig()
    mw.show()

def showAgreementScreen(d):
    mw.hide()
    #d.close()
    a = agreement_ui.Ui_Dialog()
    dial = QDialog(d)
    dial.accepted.connect(lambda:agreeAgreement())
    dial.rejected.connect(lambda:app.exit())
    dial.closeEvent = lambda:app.exit()
    a.setupUi(dial)
    dial.show()

def showAboutScreen(d):
    closeDialog(d)
    a = about_ui.Ui_Dialog()
    dial = QDialog(d)
    a.setupUi(dial)
    a.textBrowser.anchorClicked.connect(lambda:showAgreementScreen(dial))
    dial.show()

def detectETSPath(sui:settings_ui.Ui_Dialog):
    setStatus("正在检测E听说路径...")
    res = utils.executableByProcess("ETSShell.exe")
    if not res:
        setStatus("检测失败","red")
        sui.label.setText("⚠请先运行E听说")
        sui.label.setStyleSheet(u"background-color: red;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"padding:2px;")
        return
    else:
        sui.etsPathE.setText(os.path.dirname(res))
        sui.label.hide()
        setStatus("检测完成")

def openSettingsDialog():
    d = QDialog(mw)
    sui = settings_ui.Ui_Dialog()
    sui.setupUi(d)
    mwui.centralwidget.setDisabled(True)
    sui.save.clicked.connect(lambda:saveSettings(sui,d))
    sui.cancel.clicked.connect(lambda:closeDialog(d))
    sui.about.clicked.connect(lambda:showAboutScreen(d))
    sui.etsPathE.setText(settings.read(str,"ets","path"))
    sui.answerDisplayTypeCB.setCurrentIndex(settings.read(int,"ets","mode",0))
    sui.showDllConsoleCB.setChecked(settings.read(bool,"dev","showDevOptions",False))
    sui.devOptions.setVisible(settings.read(bool,"dev","showDevOptions",False))
    sui.CheckBox.checkStateChanged.connect(lambda:sui.devOptions.setVisible(sui.CheckBox.isChecked()))
    sui.detectETSPathBtn.clicked.connect(lambda:threading.Thread(target=lambda:detectETSPath(sui)).start())
    d.closeEvent = lambda e:closeDialog(d)
    if utils.isValidDir(settings.read(str,"ets","path")):
        sui.label.hide()
    d.show()

def saveSettings(dialog:settings_ui.Ui_Dialog,d:QDialog):
    settings.set("ets","path",dialog.etsPathE.text())
    settings.set("ets","mode",dialog.answerDisplayTypeCB.currentIndex())
    settings.saveConfig()
    closeDialog(d)
    
def setStatus(text:str,color:str="rgb(0, 121, 14)"):
    mwui.status_lb.setText(text)
    mwui.status_lb.setStyleSheet(f'''
color:#fff;
border-radius:5px;
background-color: {color};
''')

logData = ""
homework_id = None

class ETSLogHandler(QThread):
    setAnswer = Signal(str)
    is_first_open = True
    def __init__(self) -> None:
        super().__init__()
    def run(self):
        global logData,homework_id
        while True:
            if self.is_first_open and utils.isValidDir(settings.read(str,"ets","path")):
                if utils.getLatestLogFile(os.path.join(settings.read(str,"ets","path"),"logs")):
                    logData = open(os.path.join(settings.read(str,"ets","path"),"logs",utils.getLatestLogFile(os.path.join(settings.read(str,"ets","path"),"logs"))),errors="ignore").read()
                    print("ETS日志解析器初始化完成！")
                    self.is_first_open=False
            if utils.isValidDir(settings.read(str,"ets","path")) and not self.is_first_open:
                if utils.getLatestLogFile(os.path.join(settings.read(str,"ets","path"),"logs")):
                    f = open(os.path.join(settings.read(str,"ets","path"),"logs",utils.getLatestLogFile(os.path.join(settings.read(str,"ets","path"),"logs"))),errors="ignore").read()
                    if not f==logData:
                        s=f[len(logData):]
                        print("[ETSLog]",s,end="")
                        if "创建实例【成功】" in s:
                            hwids = re.findall(constants.REGS.ETS_HOMEWORK_ID,logData)
                            homework_id = hwids[-1]
                            self.setAnswer.emit(generateAnswers(os.path.join(constants.ETS_CACHE_PATH,homework_id)))
                            setStatus(f"状态：正在作业中,ID={homework_id}")
                        if "销毁实例【成功】" in s:
                            setStatus("状态：未启动")
                        logData=f

def save():
    res = QFileDialog.getSaveFileName(mw,"保存答案",".","TXT文件 (*.txt)","PDF文件 (*.pdf)")
    if not res[0]=="":
        f=open(res[0],"w",encoding="utf-8")
        f.write(mwui.textBrowser.toPlainText())
        f.close()

if __name__ == "__main__":
    #print(generateAnswers(r"C:\Users\qq\AppData\Roaming\ETS\32104"))
    global mw,mwui,app
    app=QApplication([])
    startBG = QPixmap(":/main/logo.png")
    startBG=startBG.scaled(400,400)
    ss = QSplashScreen(startBG)
    ss.setFixedSize(400,400)
    ss.show()
    mw= QMainWindow()
    mwui=Ui_MainWindow()
    mwui.setupUi(mw)
    mwui.textBrowser.write = Signal()
    mwui.settingsBtn.clicked.connect(openSettingsDialog)
    mw.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    mwui.copyBtn.clicked.connect(lambda:app.clipboard().setText(mwui.textBrowser.toPlainText()+"由E听说外挂自动生成"))
    mwui.exportBtn.clicked.connect(save)
    if not utils.isValidDir(settings.read(str,"ets","path")):
        setStatus("请设置E听说路径以自动检测答案路径！","rgb(189, 167, 0)")
    etslh = ETSLogHandler()
    etslh.setAnswer.connect(lambda s:mwui.textBrowser.setText(s))
    etslh.start()
    time.sleep(5)
    if not settings.read(bool,"agreement","agreed",False):
        showAgreementScreen(mw)
    else:
        mw.show()
    ss.finish(mw)
    app.exec()