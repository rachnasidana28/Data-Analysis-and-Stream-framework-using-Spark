import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import sys
import random
import time;

consumer_key = 'XX'
consumer_secret = 'XX'
access_token = 'XX'
access_secret = 'XX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweetScrapperOutput.json', 'a') as f:
			tweetText = json.loads(data)['text']
			tweet = ''.join([i if ord(i) < 128 else '' for i in tweetText])
			tweet = json.dumps(tweet)
			f.write(tweet + "\n")
			print (tweet)
        except BaseException as e:
            print ("Error on_data: " + str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(languages=["en"], track=['#obama','#trump'])
