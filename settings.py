import configparser
import os
import utils

cp = configparser.ConfigParser()

class settings:
    def saveConfig():
        f=open("config.ini","w")
        cp.write(f)
        f.close()
    def read(T,s,k,default=None):
        if T==bool:
            return utils.boolFromStr(cp.get(s,k,fallback=default))
        elif T==int:
            return int(cp.get(s,k,fallback=default))
        elif T==str:
            return cp.get(s,k,fallback=default)
        return None
    def set(s,k,v):
        if not cp.has_section(s):
            cp.add_section(s)
        cp.set(s,k,str(v))

if os.path.isfile("config.ini"):
    cp.read("config.ini")
else:
    cp.add_section("agreement")
    cp.set("agreement","agreed","false")
    cp.add_section("ets")
    settings.saveConfig()