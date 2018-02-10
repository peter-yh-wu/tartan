# http://python-twitter.readthedocs.io/en/latest/twitter.html

import os
import twitter
from gtts import gTTS

statuses = api.GetUserTimeline(screen_name='Beyonce') # user id
message_00 = statuses[0].text

tts = gTTS(text=message_00, lang='ja', slow=False)
tts.save("message_00.mp3")
# os.system("say hello")
os.system("mpg321 message_00.mp3")
