import ctypes, os, datetime
from pathlib import Path
import os.path

def setup_check():
    path = str(Path.home()/"AP_Debugger")
    isdir = os.path.isdir(path)
    if isdir == False:
        os.mkdir(path)
        log = open(path + '/Requirements.txt','w')
        os.chflags(path + '/Requirements.txt', 32768)
        log.write("Setup completed:     " + datetime.date.today().strftime("%m/%d/%y") + " " + datetime.datetime.now().strftime("%H:%M"))





