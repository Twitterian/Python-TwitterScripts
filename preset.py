#import platform
import os
import configparser

def ChangeCodepage():
    #if platform.system() == 'Windows':
    os.system('chcp 65001')

config = configparser.ConfigParser()
with open('config.ini', 'r', encoding='utf-8') as f:
    config.read_file(f)
if config.has_section('Console'):
    if(config['Console']['ChangeCodepage'] == 'True'):
        ChangeCodepage()
else:
    res = input("do you want change codepage setting? (yes to 'y') : ")

    if(res == 'y'):
        chcp = True
        ChangeCodepage()
    else:
        chcp = False

    config.add_section('Console');
    config.set('Console', 'ChangeCodepage', str(chcp))

    with open("config.ini", "w") as configfile:
        config.write(configfile)
