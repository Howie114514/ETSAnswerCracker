import os

ETS_CACHE_PATH = os.path.join(os.getenv("APPDATA"),"ETS")

class REGS:
    ETS_HOMEWORK_ID=r"(?<=AppData\\Roaming\\ETS\\)\d+"