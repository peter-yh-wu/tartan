import tweepy
import random
from flask import Flask
from flask import jsonify
from flask import request
from gtts import gTTS

from azure.storage.blob import BlockBlobService

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
app.config.from_pyfile('config.py')
account = app.config['ACCOUNT']   # Azure account name
key = app.config['STORAGE_KEY']      # Azure Storage account access key
container = app.config['CONTAINER'] # Container name

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	file = request.files['file']
    	filename = file.filename
        try:
            blob_service.create_blob_from_stream(container, filename, file)
        except Exception:
            print 'Exception=' + Exception
            pass
        ref =  'http://'+ account + '.blob.core.windows.net/' + container + '/' + filename
        return '''
	    <!doctype html>
	    <title>File Link</title>
	    <h1>Uploaded File Link</h1>
	    <p>''' + ref + '''</p>
	    <img src="'''+ ref +'''">
	    '''
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/api/speak', methods=['GET'])
def speak():
    message = 'Hi hamburger!'
    tts = gTTS(text=message, lang='ja', slow=False)
    tts.save("message_00.mp3")
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
