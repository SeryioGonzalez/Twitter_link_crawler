import sys

from keywords import *
from helpers import *

tweetAckMin = 2
 
if len(sys.argv) == 2:	
	tweetAckMin=int(sys.argv[1])
 
#API CONNECTION
API = twitter_setup()

#GET REQUIRED DATA FROM TWEETS
processedTweets = []
tweetSet = set()

for keyword in keywords:
	#Look for tweets from a given keyword
	keywordTweets = API.search(q='#'+keyword, tweet_mode='extended')
	#Get tuples with keyword and relevant tweet data tweet
	processedTweetBatch = [ filterTweetData(rawTweet, keyword) for rawTweet in keywordTweets ]
	#Add those tweets to the collections
	processedTweets += processedTweetBatch


linkSet = set( tweet['link'] for tweet in processedTweets if tweet['link'] != None and tweet['acks'] > tweetAckMin  )

for link in linkSet:
	print("Opening link {}".format(link))
	openBrowserTab(link)
