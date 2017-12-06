from pymongo import MongoClient
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from emoji import UNICODE_EMOJI


client = MongoClient('localhost', 27017)
db = client['usa_db']
collection = db['usa_tweets_collection']
tweets_iterator = collection.find()


#count emoji occurences
'''
d = dict()
i = 0
for tweet in tweets_iterator:
  for word in list(tweet['text']):
    if word in UNICODE_EMOJI:
      try:
        d[word] += 1
      except KeyError:
        d[word] = 1

d = sorted(d.items(), key=lambda x: -x[1])
print(d[:15])
'''

#count specific emoji usage per state
'''
d = dict()
i = 0
for tweet in tweets_iterator:
  for word in list(tweet['text']):
    if word in UNICODE_EMOJI:
      if word == '🎄' and tweet['user']['location'] is not None:
        if ',' in list(tweet['user']['location']):
          state = tweet['user']['location'].split(',')[1]
          try:
            d[state] += 1
          except KeyError:
            d[state] = 1
        
d = sorted(d.items(), key=lambda x: -x[1])
print(d[:5])
'''

'''
#count emoji usage for MA
d = dict()
i = 0
for tweet in tweets_iterator:
  for word in list(tweet['text']):
    if word in UNICODE_EMOJI and tweet['user']['location'] is not None:
      if ',' in list(tweet['user']['location']):
          state = tweet['user']['location'].split(',')[1]
          if state == 'MA' or state == 'Massachussetts' or state == ' MA' or state == ' Massachussetts' or state == 'MA ' or state == 'Massachussetts ' or state == ' MA ' or state == ' Massachussetts ':
            try:
              d[word] += 1
            except KeyError:
              d[word] = 1

d = sorted(d.items(), key=lambda x: -x[1])
print(d[:5])
'''

'''
#count emoji usage per state
d = dict()
i = 0
for tweet in tweets_iterator:
  for word in list(tweet['text']):
    if word in UNICODE_EMOJI:
      if tweet['user']['location'] is not None:
        if ',' in list(tweet['user']['location']):
          state = tweet['user']['location'].split(',')[1]
          try:
            d[state] += 1
          except KeyError:
            d[state] = 1
        
d = sorted(d.items(), key=lambda x: -x[1])
print(d[:5])
'''

#top tweeting states
'''
d = dict()
i = 0
for tweet in tweets_iterator:
  if tweet['user']['location'] is not None:
    if ',' in list(tweet['user']['location']):
      state = tweet['user']['location'].split(',')[1]
      try:
        d[state] += 1
      except KeyError:
        d[state] = 1
        
d = sorted(d.items(), key=lambda x: -x[1])
print(d[:5])
'''


#top tweeting cities in CA
'''
d = dict()
i = 0
for tweet in tweets_iterator:
  if tweet['user']['location'] is not None:
    if ',' in list(tweet['user']['location']):
      state = tweet['user']['location'].split(',')[1]
      if state == 'CA' or state == ' CA' or state == ' California' or state == 'California':
        city = tweet['user']['location'].split(',')[0]
        print(city)
        try:
          d[city] += 1
        except KeyError:
          d[city] = 1
        
d = sorted(d.items(), key=lambda x: -x[1])
print(d[:5])
'''

#sentiment analysis      
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

  #print some of the tweet content
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

