# http://python-twitter.readthedocs.io/en/latest/twitter.html

import os
import twitter
from gtts import gTTS

api = twitter.Api(consumer_key='7r2eXtOYae9rh73hntdmykKa7',
  consumer_secret='SiMKTMFvwTZDcwbBstzggOprAE2LNMblN8PIn9PmSONJNseQg0',
    access_token_key='962236458202517504-qTNen7xpBuo5RsDwQPSw3Qw3oRpYFxD',
    access_token_secret='VsEOPcSZ51NG07kdWXoqQPn24JetNsRBlO2PmE1DghxYt')

statuses = api.GetUserTimeline(screen_name='Beyonce') # user id
message_00 = statuses[0].text

tts = gTTS(text=message_00, lang='ja', slow=False)
tts.save("message_00.mp3")
# os.system("say hello")
os.system("mpg321 message_00.mp3")
