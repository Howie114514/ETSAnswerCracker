import os
import psutil
import re

def getLatestLogFile(dir):
    d = os.listdir(dir)
    d.sort(key=lambda f:os.path.getmtime(os.path.join(dir,f)))
    d.reverse()
    for f in d:
        if re.match("shell_.*\\.log",f):
            return f
    return None

def boolFromStr(s:str):
    if s=="true":
        return True
    return False

def executableByProcess(regexp=".*"):
    processes = psutil.process_iter()
    for process in processes:
        if re.match(regexp,process.name()):
            return process.exe()
        
def isValidDir(p):
    return (p and os.path.isdir(p))

def run(*funcs,args=[]):
    for f in funcs:
        f(*args)

def runIf(a,*funcs,args=[]):
    if a:
        run(*funcs,args=args)