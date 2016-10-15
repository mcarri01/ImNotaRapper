import os
import sys
import oauth2 as oauth
import json
import requests
import re

def get_sentiment(search):
	# Our keys bby
	CONSUMER_KEY = "ehAudXAxn29MEFE9JdWNoNK35"
	CONSUMER_SECRET = "7zE9qGclS7tl2yP7NQIHu3foPK1X9pB2xEv84I6snaciW7VCsF"
	ACCESS_KEY = "787097573412704256-8rSKAGiPRNEBX0bGZDaKJH7JJV8LcTQ"
	ACCESS_SECRET = "D7xBGZ0Q8xB6XqYk2q85HN7fWIkfWjVgyb09aCBFLMz1J"

	# Set up connection
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
	client = oauth.Client(consumer, access_token)

	endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=" + search + "&count=1"
	response, data = client.request(endpoint)
	tweets = json.loads(data)
	value = 0
	for tweet in tweets['statuses']:
		#text = emoji_pattern.sub(r'', tweet['text'])
		text = tweet['text']
		response = requests.post('http://text-processing.com/api/sentiment/', data={u'text': text})
		sentiment = json.loads(response.text)
		print(sentiment['label'])
		print(sentiment['probability'])
		if sentiment['label'] == 'pos':
			value = 0
		elif sentiment['label'] == 'neg':
			value = 1
		else:
			value = 0.5
	print(value)
	return value

