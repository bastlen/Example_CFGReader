import configparser as cp

class CFGHandler:
    """ Read INI-Files"""

def __init__(self,cfg_name):
    self.cfg_name = cfg_name

def getCFG(path):
    try:
        return cp
    except:
        print("Error File I/O!")
