#!/usr/bin/python2
# -*- coding:utf-8 -*-
from twython import Twython
from datetime import date, datetime, timedelta
import time
import os
from os import listdir
import random
from os.path import isfile, join
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
delay = int(config['Nick Namer']['Delay'])

# script body
mypath = "Profile Image Change.Images"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

while(len(files)) :
    filename = files[random.randrange(0, len(files))]
    try :
        with open(mypath + '/' + filename, 'rb') as image:
            twitter.update_profile_image(image=image)
            print ('changed profile image to ' + filename)
    except :
        print ('error occured ' + filename)
    time.sleep(delay)
