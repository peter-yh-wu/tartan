import tweepy
import random
from flask import Flask
from flask import jsonify
from flask import request

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

# Starting Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/api/speak',gethods=['GET'])
def speak():
    return 'Hi!'

@app.route('/api/trends', methods=['GET'])
def trends():
    trends = api.trends_available()
    finalTrends = random.sample(trends, 10)
    return jsonify(finalTrends)

@app.route('/api/tweets', methods=['GET'])
def tweets():
    tweets = api.trends_place(request.args.get('id', ''))
    return jsonify(tweets)

if __name__ == '__main__':
    app.run()
