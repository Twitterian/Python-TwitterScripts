#!/usr/bin/python2
# -*- coding:utf-8 -*-
from twython import Twython
import time
import random
import configparser

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

twitter = Twython(
    config['TwitterOauth']['AppToken'],
    config['TwitterOauth']['AppSecret'],
    config['TwitterOauth']['UserToken'],
    config['TwitterOauth']['UserSecret']
)
namebase = config['Nick Namer']['NameFormat']
delay = int(config['Nick Namer']['Delay'])

with open('Nick Namer.Emojis.txt', 'r', encoding='utf8') as emojis:
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
