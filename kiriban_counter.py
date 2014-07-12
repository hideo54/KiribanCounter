#coding: utf-8
import tweepy
import datetime

consumer_key = '************'
consumer_secret = '************'
access_token = '************'
access_token_secret = '************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.me().statuses_count
ketasu = len(str(tweets))

if (tweets + 1) % 100 == 0:
    api.update_status('just %d tweets!' % (tweets + 1))

elif ketasu != 1:
    zoro = 0
    for i in range(ketasu+1):
        zoro += 10 ** i

    if (tweets + 1) % zoro == 0 and (tweets + 1) / zoro != 9:
        api.update_status('just %d tweets!' % (tweets + 1))
