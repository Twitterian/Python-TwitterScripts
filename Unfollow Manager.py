﻿#!/usr/bin/python2
# -*- coding:utf-8 -*-
from twython import Twython
from datetime import date, datetime, timedelta
from Twitterian import Friendships;
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
friends = Friendships.GetFriendships(twitter);
followers = Friendships.GetFollowers(twitter);

print 'following : %d, follower : %d\n' % (len(friends), len(followers))

for user in friends :
    if(user in followers) : continue
    else :
        suser = twitter.show_user(user_id=user)
        twitter.destroy_friendship(screen_name=user['screen_name'])
        print "unfollowd %s(%d)" % (suser["screen_name"], user);

print "\n" + str(blocker.unfollowedUserCount) + "user(s) unfollowed."
