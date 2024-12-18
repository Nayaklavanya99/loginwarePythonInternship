import cv2
from cv2 import imshow
import time
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
    while True:
        

        result, frame = camera.read()
        cv2.putText(frame, str(time.ctime()), (20, frame.shape[0]-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (211, 211, 211), 1)
        if not result:
            print("Unable to capture the frame")
            break
        out.write(frame)
        
 
        imshow("Video Capture", frame)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            # cv2.imwrite("captured_frame.jpg", frame) 
            print("video saved")
            break
        elif key == ord('c'):
            print("Capture cancelled")
            break
    out.release()
            
camera.release()
cv2.destroyAllWindows()
