from twython import Twython

def GetFriendships(twitter):
    friends = []
    username = twitter.verify_credentials()['screen_name']
    next_cursor = -1
    while next_cursor:
        get_friends = twitter.get_friends_ids(
            screen_name=username, count=200, cursor=next_cursor)
        for friend in get_friends["ids"]:
            friends.append(friend)
            next_cursor = get_friends["next_cursor"]
    return friends

def GetFollowers(twitter):
    followers = []
    username = twitter.verify_credentials()['screen_name']
    next_cursor = -1
    while next_cursor:
        get_followers = twitter.get_followers_ids(
            screen_name=username, count=200, cursor=next_cursor)
        for follower in get_followers["ids"]:
            followers.append(follower)
            next_cursor = get_followers["next_cursor"]
    return followers
