from gtts import tts
import os
from gtts import gTTS
from os import system
import time
from cv2 import waitKey



text = "heloo"
tts = gTTS(text=text, lang='kn')

aud = f"audio/{time.ctime().replace(' ', '_').replace(':','_')}.mp3"
tts.save(aud)
os.system(f"start {aud}")
# Fix indentation and undefined waitKey function
  # Add import for waitKey
while True:
      
    key = waitKey(1) 
    if key == ord('q'):
        print("video saved")
        os.system(f"stop {aud}")
        break
    

