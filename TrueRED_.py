#!/usr/bin/python2
# -*- coding:utf-8 -*-
from twython import Twython
from datetime import date, datetime, timedelta
import os
from twython import TwythonStreamer
import configparser
import random

config = configparser.ConfigParser()
try:
    with open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)
except FileNotFoundError :
    thats = 'too bad'
while config.has_section('TwitterOauth') == False :
    os.system("OAuth.py")
config.read('config.ini')
consumer_key = config['TwitterOauth']['AppToken']
consumer_secret = config['TwitterOauth']['AppSecret']
access_token = config['TwitterOauth']['UserToken']
access_token_secret = config['TwitterOauth']['UserSecret']
if config.has_section('TrueRED_') == False :
    ownerid = input('input your owner screen name : ')
    config.add_section('TrueRED_')
    config.set('TrueRED_','OwnerID', ownerid)
    with open("config.ini", "w") as configfile:
        config.write(configfile)
else:
    ownerid = config['TrueRED_']['OwnerID']

with open('TrueRED_.input.public.txt', 'r', encoding='utf8') as fip:
    input_public = fip.readlines()
with open('TrueRED_.input.mention.txt', 'r', encoding='utf8') as fim:
    input_mention = fim.readlines()
with open('TrueRED_.output.public.txt', 'r', encoding='utf8') as fop:
    output_public = fop.readlines()
with open('TrueRED_.input.mention.txt', 'r', encoding='utf8') as fom:
    output_mention = fom.readlines()

# script body
twitter = Twython( consumer_key, consumer_secret, access_token, access_token_secret )
currentuser = twitter.verify_credentials()
print('Authenticated User : ' + currentuser['screen_name'])
print('Owner : ' + ownerid)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        try:
            if 'text' in data:
                text = data['text']
                print(text)
                if not 'retweeted_status' in data and data['user']['id'] != currentuser['id']:
                        if not 'in_reply_to_status_id' in data: # public tweet
                            for value in input_public:
                                if value in text:
                                    output = output_public[random.randrange(0, len(output_public))]
                                    twitter.update_status(status='@' + data['user']['screen_name'] + ' ' + output, in_reply_to_status_id=data['id'])
                        elif '@' + currentuser['screen_name'].lower() in text.lower(): # mention to me
                            for value in input_mention:
                                if value in text:
                                    output = output_mention[random.randrange(0, len(output_mention))]
                                    twitter.update_status(status='@' + data['user']['screen_name'] + ' ' + output, in_reply_to_status_id=data['id'])
        except Exception as e:
            print ('error : ' + str(status_code))
            twitter.update_status(status='@' + ownerid + ' ' + str(e))

    def on_error(self, status_code, data):
        try:
            print ('error : ' + str(status_code) + ':' + data['text'])
            twitter.update_status(status='@' + ownerid + ' ' + str(status_code) + ':' + data['text'])
        except Exception as e:
            twitter.update_status(status='@' + ownerid + ' ' + str(status_code))
            raise
streamer = MyStreamer( consumer_key, consumer_secret, access_token, access_token_secret )
streamer.user(replies='all')
