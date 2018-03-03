from pymongo import MongoClient
from emoji import UNICODE_EMOJI
import pandas as pd

client = MongoClient('localhost', 27017)
db = client['usa_db']
collection = db['usa_tweets_collection']
tweets_iterator = collection.find()

all_emojis = []
for tweet in tweets_iterator:
  for ch in list(tweet['text']):
    if ch in UNICODE_EMOJI and ch not in all_emojis:
      all_emojis.append(ch)

d = dict([x, []] for x in all_emojis)
res = pd.DataFrame.from_dict(data=d)

print(res.head())

tweets_iterator = collection.find()
for emo in list(res.columns):
  i = 20000
  emoji_presence = []
  tweets_iterator = collection.find()
  for tweet in tweets_iterator:
    if i <= 1000:
      if str(emo) in tweet['text']:
        emoji_presence.append(1)
      else:
        emoji_presence.append(0)
    i -= 1
  res.loc[:,emo] = emoji_presence

print(res.head())

res.to_csv('./emojis.csv', index = False)
print()
check = pd.read_csv('./emojis.csv')
print(check.head())


i = 20000
location = []
for tweet in tweets_iterator:
  if i <= 1000:   
    if tweet['coordinates']:
      location.append(1)
    else:
      location.append(0)
  i-=1

print(len(location))
print()
print(len(res.iloc[:,0]))
print()
res.loc[:,'location'] = location    
  
print(res.head())

res.to_csv('./emojis.csv', index = False)
print()
check = pd.read_csv('./emojis.csv')
print(check.head())

