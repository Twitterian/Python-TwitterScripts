#!/usr/bin/python2
# -*- coding:utf-8 -*-
from twython import Twython
import time
import random
import configparser
import os

os.system("preset.py")
# read configs
config = configparser.ConfigParser()
config.read('config.ini')
while config.has_section('TwitterOauth') == False :
    os.system("OAuth.py")
    config.read('config.ini')
twitter = Twython(
    config['TwitterOauth']['AppToken'],
    config['TwitterOauth']['AppSecret'],
    config['TwitterOauth']['UserToken'],
    config['TwitterOauth']['UserSecret']
)

if config.has_section('NickNamer'):
    namebase = config['NickNamer']['NameFormat']
    delay = int(config['NickNamer']['Delay'])
else:
    namebase = input("set your name base : ")
    delay = int(input("set delay secont : "))
    config.add_section('NickNamer');
    config.set('NickNamer', 'NameFormat', namebase)
    config.set('NickNamer', 'Delay', str(delay))
    with open("config.ini", "w") as configfile:
        config.write(configfile)


with open('NickNamer.Emojis.txt', 'r', encoding='utf8') as emojis:
    additionals = emojis.readlines()

# script body

while(len(additionals)) :
    additional = additionals[random.randrange(0, len(additionals))]
    try :
        newname = namebase + additional
        twitter.update_profile(name=newname)
        print ('changed username to : ' + newname)
    except :
        print ('error occured : ' + additional)
    time.sleep(delay)
