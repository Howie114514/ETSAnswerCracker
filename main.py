import enum
import os
import threading
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main_ui import Ui_MainWindow
import selectFile_ui
import utils
import constants
import settings_ui
import about_ui
import agreement_ui
import json
from settings import settings
import re
import toast
import main_rc

dynamicThemes = False
themes=["light","dark"]
currentTheme = settings.read(str,"program","theme","light")

def applyTheme(o):
    theme = settings.read(str,"program","theme","light")
    if dynamicThemes:
        o.setStyleSheet(open(os.path.join("./themes/",theme+".css")).read())
    else:
        f=QFile(":/main/themes/"+theme+".css")
        f.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        o.setStyleSheet(f.readAll().toStdString())

def answerTxt(a,all):
    return f"""<span title="当前为最短答案，答案还可以是：{{}}">{a}</span>""".format("\n- "+"\n- ".join(all))

def generateAnswersHTML(dir):
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
    num=1
    res='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li { white-space: pre-wrap; }
li.unchecked::marker { content: "\2610"; }
li.checked::marker { content: "\2612"; }
hr{color:#ccc}
</style></head><body style=" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;">'''
    for c in contents:
        print(c)
        
        content = json.load(open(os.path.join(c,"content.json"),encoding="utf-8"))
        if content["structure_type"]=="collector.read":
            print("模仿朗读：",c)
            res+="<h4 style=\"margin:0px;padding:0px;border:0px\">"+str(num)+"：模仿朗读</h4>"
            res+=content["info"]["value"]
            res+="<br>"
        elif content["structure_type"]=="collector.picture":
            print("复述：",c)
            res+="<h4 style=\"margin:0px;padding:0px;border:0px\">"+str(num)+"：短文复述</h4>"
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
        elif content["structure_type"]=="collector.role":
            print("信息获取/提问：",c)
            res+="<h4 style=\"margin:0px;padding:0px;border:0px\">"+str(num)+"：信息获取/提问</h4>"
            n=1
            for q in content["info"]["question"]:
                res+="<font color=gray>("+str(n)+") </font>"
                std = q["std"]
                answer = ""
                allAnswers = []
                for a in std:
                    allAnswers.append(a["value"])
                    if settings.read(int,"ets","mode",0)==1:
                        answer+=a["value"]+"<br>"
                    else:
                        if len(a["value"])<len(answer):
                            answer=a["value"]
                        elif answer=="":
                            answer=a["value"]
                if settings.read(int,"ets","mode",0)==0:
                    answer = answerTxt(answer,allAnswers)
                res+=answer
                n+=1
                res+="<br>"
            res+="<br>"
            
        num+=1
    res+="</body></html>"
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
    applyTheme(dial)
    dial.accepted.connect(lambda:agreeAgreement())
    dial.rejected.connect(lambda:app.exit())
    dial.closeEvent = lambda:app.exit()
    a.setupUi(dial)
    dial.show()

def showAboutScreen(d):
    closeDialog(d)
    a = about_ui.Ui_Dialog()
    dial = QDialog(d)
    applyTheme(dial)
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
    applyTheme(d)
    sui = settings_ui.Ui_Dialog()
    sui.setupUi(d)
    mwui.centralwidget.setDisabled(True)
    sui.save.clicked.connect(lambda:saveSettings(sui,d))
    sui.cancel.clicked.connect(lambda:closeDialog(d))
    sui.about.clicked.connect(lambda:showAboutScreen(d))
    sui.etsPathE.setText(settings.read(str,"ets","path"))
    sui.answerDisplayTypeCB.setCurrentIndex(settings.read(int,"ets","mode",0))
    sui.themeCB.clear()
    sui.themeCB.addItems(themes)
    sui.themeCB.setCurrentIndex(themes.index(settings.read(str,"program","theme","light")))
    sui.detectETSPathBtn.clicked.connect(lambda:threading.Thread(target=lambda:detectETSPath(sui)).start())
    d.closeEvent = lambda e:closeDialog(d)
    if utils.isValidDir(settings.read(str,"ets","path")):
        sui.label.hide()
    d.show()

def saveSettings(dialog:settings_ui.Ui_Dialog,d:QDialog):
    global currentTheme
    settings.set("ets","path",dialog.etsPathE.text())
    settings.set("ets","mode",dialog.answerDisplayTypeCB.currentIndex())
    settings.set("program","theme",dialog.themeCB.currentText())
    if not settings.read(str,"program","theme","light")==currentTheme:
        currentTheme = settings.read(str,"program","theme","light")
        print("重载主题")
        applyTheme(app)
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
                            self.setAnswer.emit(generateAnswersHTML(os.path.join(constants.ETS_CACHE_PATH,homework_id)))
                            setStatus(f"状态：正在作业中,ID={homework_id}")
                        if "销毁实例【成功】" in s:
                            setStatus("状态：未启动")
                        logData=f

def openSelectDirDialog():
    f=selectFile_ui.Ui_Dialog()
    d = QDialog(mw)
    applyTheme(d)
    f.setupUi(d)
    f.list.addItems(os.listdir(constants.ETS_CACHE_PATH))
    f.list.itemDoubleClicked.connect(lambda i:utils.run(lambda i:mwui.textBrowser.setHtml(generateAnswersHTML(os.path.join(constants.ETS_CACHE_PATH,i.text()))),lambda x:d.close(),args=[i]))
    d.show()

def save():
    res = QFileDialog.getSaveFileName(mw,"保存答案",".","TXT文件 (*.txt)","PDF文件 (*.pdf)")
    if not res[0]=="":
        f=open(res[0],"w",encoding="utf-8")
        f.write(mwui.textBrowser.toPlainText())
        f.close()

nogui=False

if __name__ == "__main__" and not nogui:
    global mw,mwui,app
    app=QApplication([])
    applyTheme(app)
    startBG = QPixmap(":/main/logo.png")
    startBG=startBG.scaled(400,400)
    ss = QSplashScreen(startBG)
    ss.setFixedSize(400,400)
    ss.show()
    mw= QMainWindow()
    mw.keyReleaseEvent = lambda ev:utils.runIf(ev.key()==Qt.Key.Key_F12,lambda:applyTheme(app))
    mwui=Ui_MainWindow()
    mwui.setupUi(mw)
    mwui.textBrowser.setOpenExternalLinks(True)
    mwui.textBrowser.setOpenLinks(True)
    mwui.settingsBtn.clicked.connect(openSettingsDialog)
    mw.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    mwui.copyBtn.clicked.connect(lambda:utils.run(lambda:app.clipboard().setText(mwui.textBrowser.toPlainText()+"由E听说外挂自动生成:https://Howie114514.github.io/etsac"),lambda:toast.sendNotification("成功","已复制到剪贴板")))
    mwui.exportBtn.clicked.connect(save)
    mwui.openFolderBtn.clicked.connect(openSelectDirDialog)
    toast.setDefaultWidget(mw.centralWidget())
    if not utils.isValidDir(settings.read(str,"ets","path")):
        setStatus("请设置E听说路径以自动检测答案路径！","rgb(189, 167, 0)")
    etslh = ETSLogHandler()
    etslh.setAnswer.connect(lambda s:utils.run(lambda:toast.sendNotification("提示","已生成答案",type=toast.ToastTypes.Info),lambda:mwui.textBrowser.setText(s)))
    etslh.start()
    if not settings.read(bool,"agreement","agreed",False):
        showAgreementScreen(mw)
    else:
        mw.show()
    ss.finish(mw)
    app.exec()