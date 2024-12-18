import cv2
from cv2 import imshow
import time
from gtts import gTTS
import os

aud = None
def playaudio(name):
    global aud
    tts = gTTS(text=f'started recording {name}', lang='en')
    aud = f"audio/{time.ctime().replace(' ', '_').replace(':','_')}.mp3"
    tts.save(aud)
    return aud
    # os.system(f"start {aud}")
    # key = cv2.waitKey(1) 
    # if key == ord('q'):
    #     print("video saved")
    #     os.system(f"stop {aud}")
name ="hello "
text = """ಇದು ಹೂವಿನ ಲೋಕವೇ.....
ಇಲ್ಲಿ ಗೆಳತಿಯರಿಲ್ಲವೆ.....
ಹೇಗೆ ನಾ ಹಾಡಲಿ......
ಹೇಳಿ ಹೂಗಳೇ.......ಏ


ಯಾರೆ ನೀನು ರೋಜ ಹೂವೆ
ಯಾರೆ ನೀನು ಮಲ್ಲಿಗೆ ಹೂವೆ
ಹೇಳೆ ಓ ಚೆಲುವೇ....
ಚೆಲುವಿನ ಹೂವೇ.....
ಸೌಗಂಧ ಹೂವಲ್ಲಿ ಕೂಡಿಕೊಂಡಿತಂತೆ
ಸೌಂದರ್ಯ ಹೆಣ್ಣಲ್ಲಿ ತುಂಬಿಕೊಂಡಿತಂತೆ
ಸಂಗೀತ ನನ್ನಲ್ಲಿ ಸೇರಿಕೊಂಡಿತಂತೆ
ಹೇ ಹೇ ಹೇ ....ಏ ಏ ಏ ಏ .......

 ಯಾರೆ ನೀನು ರೋಜ ಹೂವೆ
ಯಾರೆ ನೀನು ಮಲ್ಲಿಗೆ ಹೂವೆ
ಹೇಳೆ ಓ ಚೆಲುವೇ...ಏ
ಚೆಲುವಿನ ಹೂವೇ.....



ಹೂವಿನಲ್ಲಿ ಹೆಣ್ಣಿನ ಅಂದ ನೋಡು
ಹೆಣ್ಣಿನಲ್ಲಿ ಹೂವಿನ ಬಣ್ಣ ನೋಡು
ಹೆಣ್ಣೇ ಹೂವೆಂದು ಪ್ರೀತಿ ಮಾಡು
ಹೆಣ್ಣಿನಲ್ಲಿ ಸಂಗೀತ ಕೇಳಿ ನೋಡು
ಸಂಗೀತಕ್ಕೆ ಸ್ಪೂರ್ತಿ ಹೆಣ್ಣು ನೋಡು
ಹೆಣ್ಣೆ ಸಂಗೀತವೆಂದು ಹಾಡು
ಅರೆ ರಬಪಾಬ ರಿಬಪಾಬ ರಬರಿಬ ರಬಪಾಬ ರಿಬಪಾಬರಬರಿಬ
ಜಾಲಿ ಮಾಡು ಲೈಫಲ್ಲಿ......
ಸೌಗಂಧ
ಸೌಂದರ್ಯ
ಸಂಗೀತ ನಿನ್ನದೂ

 ಯಾರೆ ನೀನು ರೋಜ ಹೂವೆ
ಯಾರೆ ನೀನು ಮಲ್ಲಿಗೆ ಹೂವೇ
ಹೇಳೆ ಓ ಚೆಲುವೇ...ಏ
ಚೆಲುವಿನ ಹೂವೇ.....

ಹುಡ್ಗಿರಿಗೆ ನಾನೇ ರಾಜ ನಾನು
ಹುಡ್ಗರಿಗೆ ಖದೀಮ ಕಳ್ಳ ನಾನು
ಪ್ರಳಯಾಂತಕ ನಾನು ಕೇಳು ನೀನು
ಲೋಕವೆಲ್ಲ ನನ್ನ ಪಾಕೆಟ್ ನಲ್ಲಿ
ಸ್ನೇಹವೆಂಬ ಲೌಲಿ ರಾಕೆಟ್ನಲ್ಲಿ
ತೇಲಿ ಹಾಡೊ ಪ್ರೇಮಿ ನಾನು
ಶಬಪಾಬ ರಿಬಪಾಬ ಶಬರಿಬ ಶಬಪಾಬ ರಿಬಪಾಬ ಶಬರಿಬ
ಕೇಳಿ ನನ್ನ ಪ್ರೇಮಿಗಳೇ
ಈ ಪ್ರೀತಿ....
ಅಭಿಮಾನ....
ಎಂದೆಂದೂ ನನ್ನದೂ.....
 ಯಾರೆ ನೀನು ರೋಜ ಹೂವೆ
ಯಾರೆ ನೀನು ಮಲ್ಲಿಗೆ ಹೂವೆ
ಹೇಳೆ ಓ ಚೆಲುವೇ...ಏ
ಚೆಲುವಿನ ಹೂವೇ
ಸೌಗಂಧ ಹೂವಲ್ಲಿ ಕೂಡಿಕೊಂಡಿತಂತೆ
ಸೌಂದರ್ಯ ಹೆಣ್ಣಲ್ಲಿ ತುಂಬಿಕೊಂಡಿತಂತೆ
ಸಂಗೀತ ನನ್ನಲ್ಲಿ ಸೇರಿಕೊಂಡಿತಂತೆ
ಹೇ ಹೇ ಹೇ ....ಏ ಏ ಏ ಏ .......

ಹ್ಹಾ...

ಹ್ಹಾ...

ಹ್ಹೇ...

ಹ್ಹೇ...

ರಾಪ ರಬಪಾಪ ರಪ


ಲಾಲಾಲಾ ಹಾ
ಲಾಲಾಲಾ ಲಾ
ಲಾಲಾಲಾ ಹೇ
ಲಾಲಾಲಾ ಹಾ

ತರದರ ತರದರ ದರದರ

ಪಾ ಪಪಪ ಪಾ ಪಪಪ ಪಾ"""
# playaudio(name) 
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Camera not found")
    exit()
else:
    # Define the codec and create videowriter object
    # fourcc = cv2.VideoWriter_fourcc(*'XVID') # For .AVI XVID
    # fourcc = cv2.VideoWriter_fourcc(*'H264') # For .MP4    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # For .MP4    
    # Specify full path to save the video file
    v = f"videos/{time.ctime().replace(' ', '_').replace(':','_')}.mp4"
    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # v = f"videos/{timestamp}.mp4"  
    out = cv2.VideoWriter(v, fourcc, 20.0, (640, 480), isColor=True)  
    val = playaudio(name) 
    os.system(f"start {val}")
    while True:
        

        result, frame = camera.read()
        
        cv2.putText(frame, name, (20, frame.shape[0]-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (211, 211, 211), 1)
        if not result:
            print("Unable to capture the frame")
            break
        out.write(frame)
        
 
        imshow("Video Capture", frame)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            print("video saved")
            os.system(f"stop {val}")
            break
        elif key == ord('c'):
            print("Capture cancelled")
            break
    out.release()
            
camera.release()
cv2.destroyAllWindows()
