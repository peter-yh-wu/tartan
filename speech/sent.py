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

def yose_emot(userid):
    '''
    returns score for the sentiment of given twitter feed
    '''
    score = 0.0
    count = 0.0

    for tweet in tweepy.Cursor(api.user_timeline,id=userid).items():
        ctxt = tweet.text
        if len(ctxt) > 0:
            cscore = emot_phrase(ctxt)
            if cscore != -1:
                score += cscore
                count += 1.0

    return (str(score/count))

def emot_phrase(phrase):
    '''
    returns a score for the sentiment of the given phrase
    if the phrase is an empty string, returns -1
    '''
    score = 0.0
    count = 0.0

    for word in phrase.split():
        s0 = swn.senti_synsets(word,'a')
        s1 = list(s0)
        if len(s1) > 0:
             score += s1[0].pos_score()
             count += 1.0

    if count == 0.0:
        return -1
    else:
        return (score/count)

print(str(yose_emot("YosemiteNPS")))
