# -*- coding: utf-8 -*-

from twython import Twython
from datetime import date, datetime, timedelta
import configparser
import webbrowser

def writeToFile(APP_TOKEN, APP_SECRET, USER_TOKEN, USER_SECRET):
        config = configparser.ConfigParser()
        config.add_section('TwitterOauth')
        config.set('TwitterOauth','AppToken', APP_TOKEN)
        config.set('TwitterOauth','AppSecret', APP_SECRET)
        config.set('TwitterOauth','UserToken', USER_TOKEN)
        config.set('TwitterOauth','UserSecret', USER_SECRET)
        with open("config.ini", "a+") as configfile:
            config.write(configfile)

print ("[1] just input myuser  token")
print ("[2] oauth with app token")
print ("")
sel = int(input("select oauth type : "))
if sel == 1:
    apptok = input("your APP_TOKEN : ")
    appsec = input("your APP_SECRET : ")
    usrtok = input("your USER_TOKEN : ")
    usrsec = input("your USER_SECRET : ")
    writeToFile(apptok, appsec, usrtok, usrsec)
elif sel == 2:
    apptok = input("your APP_TOKEN : ")
    appsec = input("your APP_SECRET : ")
    twitter = Twython(apptok, appsec)
    auth = twitter.get_authentication_tokens()
    webbrowser.open(auth["auth_url"], new=2)
    captcha = input("input captcha : ")
    twitter = Twython(apptok, appsec, auth['oauth_token'], auth['oauth_token_secret'])
    final = twitter.get_authorized_tokens(captcha)
    writeToFile(apptok, appsec, final['oauth_token'], final['oauth_token_secret'])
else:
    print ("are you kidding me?")
