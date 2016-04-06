from twython import Twython

def Unfollow(twitter, user):
    twitter.destroy_friendship(screen_name=user['screen_name'])

def Block(twitter, user):
    twitter.create_block(screen_name=user['screen_name'])

def BlockUnblock(twitter, user):
    twitter.create_block(screen_name=user['screen_name'])
    twitter.destroy_block(screen_name=user['screen_name'])

def Follow(twitter, user):
    twitter.create_friendship(screen_name=user['screen_name'])
