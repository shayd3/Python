import tweepy
from textblob import TextBlob

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('philadelphia')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) #Polarity is how + or -, subjectivity is if it's more of an opinion or factual
	print