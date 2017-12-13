from emoji import UNICODE_EMOJI, emojize
import folium
import urllib.request, re
from pymongo import MongoClient
import webbrowser
from selenium import webdriver


client = MongoClient('localhost', 27017)
db = client['usa_db']
collection = db['usa_tweets_collection']
tweets_iterator = collection.find()


def count(mylist):
    d = dict()
    for item in mylist:
        try:
            d[item] += 1
        except:
            d[item] = 1

    d = sorted(d.items(), key=lambda x: -x[1])
    return [x[0] for x in d]

#get top 2 emojis per state
d1 = dict()
d2 = dict()
for tweet in tweets_iterator:
    if tweet['user']['location'] and ',' in tweet['user']['location']:
        for ch in list(tweet['text']):
            if ch in UNICODE_EMOJI:
                state = tweet['user']['location'].split(',')[1]
                if state.lower() == 'fl' or state.lower() == ' fl':
                    if tweet['coordinates']:
                        d2[state] = tweet['coordinates']['coordinates']
                    try:
                        d1[state].append(ch)
                    except:
                        d1[state] = [ch]


for key in d1:
    d1[key] = count(d1[key])[:100]
    print(d1[key])

mymap = folium.Map(location=[45.372, -121.6972], zoom_start=4)

for key in d1:
    for emo0 in d1[key]:
        #emo0 = d1[key][0]
        print(emo0)
        try:
            site = 'https://emojipedia.org/'+ emojize(emo0)
            browser = webdriver.Chrome('./chromedriver')
            browser.get(site)
            html_source = browser.page_source
            links = re.findall('https://emojipedia-us.s3.amazonaws.com/thumbs/120/apple/118/.+.png', html_source)
            link = links[0].split('.png')[0] + '.png'
            print('link = ', link)
            icon_url = folium.features.CustomIcon(link)
            print(d2[key])
            folium.Marker(location=list(reversed(d2[key])), icon=icon_url).add_to(mymap)
        except Exception as e:
            print('failed ', e)

mymap.save('emojiMapMiami.html')

