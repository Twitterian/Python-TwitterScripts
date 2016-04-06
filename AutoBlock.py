#!/usr/bin/python2
# -*- coding:utf-8 -*-

from twython import Twython
from datetime import date, datetime, timedelta
from Twitterian import Friendships
import configparser
import os

os.system("preset.py")
# read configs
config = configparser.ConfigParser()
with open('config.ini', 'r', encoding='utf-8') as f:
    config.read_file(f)
while config.has_section('TwitterOauth') == False :
    os.system("OAuth.py")
    config.read('config.ini')
twitter = Twython(
    config['TwitterOauth']['AppToken'],
    config['TwitterOauth']['AppSecret'],
    config['TwitterOauth']['UserToken'],
    config['TwitterOauth']['UserSecret']
)

# script body
defaultUrlContainString = "default_profile_images"
if config.has_section('AutoBlock'):
    minAllowStatusCount = int(config['AutoBlock']['MinStatusCount']) # Minimum tweet count for don't block
    minCreateDay = int(config['AutoBlock']['MinCreateDay']) # Minimum tweet count for don't block
else:
    minAllowStatusCount = int(input('set minimum status count : '))
    minCreateDay = int(input('set minimum create days : '))
    config.add_section('AutoBlock');
    config.set('AutoBlock', 'MinStatusCount', str(minAllowStatusCount))
    config.set('AutoBlock', 'MinCreateDay', str(minCreateDay))
    with open("config.ini", "w") as configfile:
        config.write(configfile)

followers = Friendships.GetFollowers(twitter);
userCnt = len(followers)
print ("successful get follower(s) list : " + str(userCnt) + "\n")

blockedUserCount = 0
for user in followers :
    if (user['statuses_count'] < minAllowStatusCount):
        twitter.create_block(screen_name=user['screen_name'])
        blockedUserCount += 1
        print ("blocked " + user['screen_name'] + "(" + user['id_str'] + ") - minimum tweet count : " + user['statuses_count'])
        continue

    if(defaultUrlContainString in user['profile_image_url']):
        twitter.create_block(screen_name=user['screen_name'])
        blockedUserCount += 1
        print ("blocked " + user['screen_name'] + "(" + user['id_str'] + ") - default profile image")
        continue

    created_at = datetime.strptime(user['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    delta = (datetime.today() - created_at).days
    if delta < minCreateDay :
        twitter.create_block(screen_name=user['screen_name'])
        blockedUserCount += 1
        print ("blocked " + user['screen_name'] + "(" + user['id_str'] + ") - minumun created date : " + str(delta))
        continue

print ("\n" + str(blockedUserCount) + "user(s) blocked.")
