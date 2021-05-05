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

with open(r"twitter_data/tweet2.csv", "r") as f:
    total = []
    total = f.readlines()
    real = []
    for n in range(len(total)):
        string = total[n]
        string = string.strip('][').split(', ', maxsplit=2)
        real.append(string)
    for i in range(len(real)):
        stringg = real[i][0]
        stringg = re.sub("'", '', stringg)
        real[i][0] = stringg
        stringg = real[i][1]
        stringg = re.sub("'", '', stringg)
        real[i][1] = stringg
        stringg = real[i][1]
        stringg = re.sub("'", '', stringg)
        real[i][2] = stringg
    print(real[1][2])
    f.close()

    text = real[0][0]
    location = real[0][1]
    date = real[0][2]

    df = pd.read_csv('twitter_data/tweet2.csv')
    print(df)