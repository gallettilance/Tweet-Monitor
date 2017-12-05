from pymongo import MongoClient
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from emoji import UNICODE_EMOJI



client = MongoClient('localhost', 27017)
db = client['usa_db']
collection = db['usa_tweets_collection']
tweets_iterator = collection.find()

d = dict()
i = 0
for tweet in tweets_iterator:
  for word in tweet['text'].split():
    if word in UNICODE_EMOJI:
      try:
        d[word] += 1
      except KeyError:
        d[word] = 1

d = sorted(d.items(), key=lambda x: -x[1])
print(d)

      
'''
client = MongoClient('localhost', 27017)
db = client['twitterdb']
collection = db['twitter_search']
tweets_iterator = collection.find()

tweetCnt = 0
locEnabled = 0
for tweet in tweets_iterator:
  if 'data' in tweet['text'].lower():
    tweetCnt += 1
    if tweet['user']['location']:
      locEnabled += 1

    blob = TextBlob(tweet['text'], analyzer=NaiveBayesAnalyzer())
    if blob.sentiment.classification == 'pos':
      print('positive sentiment for the tweet: ', tweet['text'])
    if blob.sentiment.classification == 'neg':
      print('negative sentiment for the tweet: ', tweet['text'])
    if blob.sentiment.classification == 'neu':
      print('neutral sentiment for the tweet: ', tweet['text'])

  
  print('tweet text: ',tweet['text'])
  print('user\'s screen name: ',tweet['user']['screen_name'])
  print('user\'s name: ',tweet['user']['name'])
  print('location: ', tweet['user']['location'])
  try:
    print('retweet count: ',tweet['retweeted_status']['retweet_count'])
    print('retweeter\'s name: ', tweet['retweeted_status']['user']['name'])
    print('retweeted\'s screen name: ', tweet['retweeted_status']['user']['screen_name'])
  except KeyError:
      pass
  

print(tweetCnt)
print()
print(locEnabled)
'''

