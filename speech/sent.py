import os
import tweepy
from gtts import gTTS
from os import listdir

from nltk.corpus import sentiwordnet as swn

# Twitter Authentication
authentication = tweepy.OAuthHandler(
    '7r2eXtOYae9rh73hntdmykKa7',
    'SiMKTMFvwTZDcwbBstzggOprAE2LNMblN8PIn9PmSONJNseQg0'
)
authentication.set_access_token(
    '962236458202517504-qTNen7xpBuo5RsDwQPSw3Qw3oRpYFxD',
    'VsEOPcSZ51NG07kdWXoqQPn24JetNsRBlO2PmE1DghxYt'
)
api = tweepy.API(authentication)

def yose_emot:
    '''51270 words'''
    score = 0
    count = 0
    for tweet in tweepy.Cursor(api.user_timeline,id='YosemiteNPS').items():
        for word in tweet.text.split():

            s0 = swn.senti_synsets(word,'a')
            s1 = list(s0)
            if len(s1) > 0:
                 score += s1[0].pos_score()
                 count += 1
    return (str(score/count))
