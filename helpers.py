import tweepy
import subprocess 
from credentials import *
from keywords import *

chromeExecutable="/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"

def twitter_setup():
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)

    return api
	
def openBrowserTab(linkInTweet):
	if linkInTweet is not None:
		return
		subprocess.run([chromeExecutable, linkInTweet])

def filterTweetData(rawTweet, keyword):
	
	jsonTweet = rawTweet._json

	tweet = {
		'link': getLinkInTweet(jsonTweet), 
		'tweetLink': 'https://twitter.com/{0}/status/{1}'.format(jsonTweet['user']['screen_name'], jsonTweet['id']),
		'keyword':keyword,
		'acks': jsonTweet['favorite_count'] + jsonTweet['retweet_count'],
		'original': not 'retweeted_status' in jsonTweet.keys() 
	}

	return tweet

def getLinkInTweet(tweet):
	link = None

	if len(tweet['entities']['urls']) == 0:
		try:
			link = tweet['retweeted_status']['entities']['urls'][0]['url']
		except Exception:
			link = None
	else:
		link = tweet['entities']['urls'][0]['expanded_url']	

	return link	