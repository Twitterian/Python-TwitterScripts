# -*- coding: utf-8 -*-

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
friends = Friendships.GetFriendships(twitter);
followers = Friendships.GetFollowers(twitter);

print('')
print('following : %d, follower : %d' % (len(friends), len(followers)))

unfollowedUserCount = 0
bubedUserCount = 0
blockedUserCount = 0
followedUserCount = 0

for user in followers:
    if user in friends:
        continue
    else:
        suser = twitter.show_user(user_id=user)
        print('----------------------------------------')
        print("Name : " + suser["name"])
        print('Username : @' + suser["screen_name"])
        print('Description : ' + suser["description"])
        print('Friends : ' + str(suser["friends_count"]) +
              "\tFollowers : " + str(suser["followers_count"]))
        print('Created at : ' + suser["created_at"])
        print('Protected : ' + str(suser["protected"]))
        print('')
        print('  [0] Do nothing')
        print('  [1] BUB this user')
        print('  [2] Block this user')
        print('  [3] Follow this user')
        print('')

        while True:
            try:
                sel = int(input("select csae : "))

                if sel == 0:
                    print("pass user @%s(%d)" % (suser["screen_name"], user))
                    break
                elif sel == 1:
                    twitter.create_block(screen_name=suser['screen_name'])
                    twitter.destroy_block(screen_name=suser['screen_name'])
                    print("block and unblock @%s(%d)" % (suser["screen_name"], user))
                    break
                elif sel == 2:
                    twitter.create_block(screen_name=suser['screen_name'])
                    print("block user @%s(%d)" % (suser["screen_name"], user))
                    break
                elif sel == 3:
                    twitter.create_friendship(screen_name=suser['screen_name'])
                    print("follow user @%s(%d)" % (suser["screen_name"], user))
                    message = input("\ndo yo wanna mention to this user? if you dont wanna, you can input empty space : ")
                    if message != '':
                        message = "@" + suser["screen_name"] + " " + message
                        twitter.update_status(status=message)
                        print("tweet [" + message + "]")
                        break
                    break
                else:
                    print("invaild input. retry.")
                    continue
            except ValueError:
                print("invaild input. retry.")


print('')
print(str(bubedUserCount) + "user(s) bubed.")
print(str(blockedUserCount) + "user(s) blocked.")
print(str(followedUserCount) + "user(s) followed.")
print('')
input("press any key to continue")
