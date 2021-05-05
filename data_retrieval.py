import requests as rq
import matplotlib.pyplot as plt
import numpy as np
import sys
import re
import tweepy
import pandas as pd
import datetime

from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def main():
    # def _get_data(subreddit, count):
    #         url = "https://www.reddit.com/r/%s/.json?count=%d" % (subreddit, count)
    #         data = rq.get(url, headers = {'User-agent': 'sneakybot'}).json()
    #         for d in data['data']['children']:
    #             print(len(d))
    #             # return d
    #         #     if (d['data']['selftext_html']) != None:
    #         #         text = d['data']['selftext_html']
    #         #         text = re.sub(r'&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;', '', text)
    #         #         text = re.sub(r"&lt;/p&gt;", '', text)
    #         #         text = re.sub(r"&lt;/div&gt;&lt;!-- SC_ON --&gt;", '', text)
    #         print("Retrieved %d posts " % count)
    #         # return data
    #         #return text


    ############################## code for retrieving tweets (lines 28 - 89) ##########################################


    consumer_key = 'RLtdRPBzFkscpOwVh163uSMpU'
    consumer_secret = 'SYsH8VhqqTbpUb86DfmKinnBhsUEoAgMAMxoJ3ay94tHsb9yLz'
    access_token = '1330857375276933127-I2tmjdbBttqtklN41Xlfsrsk7JE1sQ'
    access_token_secret = 'VkeE142e3c2cpkLsJZF5WWrviiSdNNWNDRGobursJHB3R'


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # lists of different parameters needed for the search
    Vaccines = ['Pfizer', 'BioNTech', 'Sinopharm', 'Sinovac', 'Moderna']
    NYC = ['New York', 'Brooklyn', 'New York City', 'Queens', 'Manhattan', 'Bronx']
    FLO = ['Florida', 'Tampa', 'Miami', 'Orlando', 'Jacksonville', 'St. Petersburg']
    TEX = ['Texas', 'Austin', 'Houston', 'Dallas', 'San Antonio', 'Fort Worth']
    CAL = ['California', 'Los Angeles', 'San Fransisco', 'San Diego', 'Fresno', 'San Jose']

    # date is 2021 because vaccine dataset starts 1/1/21
    early_date = '2021-05-03'


    #lists that have the tweets, dates, and locations
    
    with open(r"twitter_data/tweet3.csv","w+") as f:
        sys.stdout = f
        print('text, location, date')
        for vacc in Vaccines:
            for place in NYC:
                for tweet in tweepy.Cursor(api.search, q=vacc, lang='en', until=early_date).items(100):
                    if re.search(place, tweet.user.location) or re.search(place, tweet.text):
                        total = []
                        total.append(tweet.text)
                        total.append('NY')
                        dat3 = tweet.created_at
                        dat3 = dat3.strftime('%Y-%m-%d')
                        total.append(dat3)
                        print(*total, sep = ", ")
            for place in FLO:
                for tweet in tweepy.Cursor(api.search, q=vacc, lang='en', until=early_date).items(100):
                    if re.search(place, tweet.user.location) or re.search(place, tweet.text):
                        total = []
                        total.append(tweet.text)
                        total.append('FL')
                        dat3 = tweet.created_at
                        dat3 = dat3.strftime('%Y-%m-%d')
                        total.append(dat3)
                        print(*total, sep = ", ")
            for place in TEX:
                for tweet in tweepy.Cursor(api.search, q=vacc, lang='en', until=early_date).items(100):
                    if re.search(place, tweet.user.location) or re.search(place, tweet.text):
                        total = []
                        total.append(tweet.text)
                        total.append('TX')
                        dat3 = tweet.created_at
                        dat3 = dat3.strftime('%Y-%m-%d')
                        total.append(dat3)
                        print(*total, sep = ", ")
            for place in CAL:
                for tweet in tweepy.Cursor(api.search, q=vacc, lang='en', until=early_date).items(100):
                    if re.search(place, tweet.user.location) or re.search(place, tweet.text):
                        total = []
                        total.append(tweet.text)
                        total.append('CA')
                        dat3 = tweet.created_at
                        dat3 = dat3.strftime('%Y-%m-%d')
                        total.append(dat3)
                        print(*total, sep = ", ")
        f.close()
    
    # with open(r"reddit_data/reddit_data.txt","w+") as f:
    #     sys.stdout = f
    #     print(_get_data("CovidVaccinated", 500))
    #     f.close()
    
    

if __name__ == "__main__":
    main()