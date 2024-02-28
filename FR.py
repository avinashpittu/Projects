import cv2
import numpy as np
import datetime
import time

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('nodcontrol.avi',fourcc, 20.0, (640,480))

question = "Are Aliens Real?"

#question = input("Ask some Question:\n ")
log_file = open("interaction_log.txt", "a")
prev_gesture = ""

#dinstance function
def distance(x,y):
    import math
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2) 
    
#capture source video
cap = cv2.VideoCapture(0)

#params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                        qualityLevel = 0.3,
                        minDistance = 7,
                        blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

#path to face cascde
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#function to get coordinates
def get_coords(p1):
    try: return int(p1[0][0][0]), int(p1[0][0][1])
    except: return int(p1[0][0]), int(p1[0][1])

#define font and text color
font = cv2.FONT_HERSHEY_SIMPLEX


#define movement threshodls
max_head_movement = 20
movement_threshold = 50
gesture_threshold = 175

#find the face in the image
face_found = False
frame_num = 0
while not face_found:
    # Take first frame and find corners in itqq
    frame_num += 1
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face_found = True
    cv2.imshow('image',frame)
    out.write(frame)
    cv2.waitKey(1)
face_center = x+w/2, y+h/3
p0 = np.array([[face_center]], np.float32)

gesture = False
x_movement = 0
y_movement = 0
gesture_show = 60 #number of frames a gesture is shown

while True:    
    ret,frame = cap.read()
    old_gray = frame_gray.copy()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    cv2.circle(frame, get_coords(p1), 4, (0,0,255), -1)
    cv2.circle(frame, get_coords(p0), 4, (255,0,0))
    
    #get the xy coordinates for points p0 and p1
    a,b = get_coords(p0), get_coords(p1)
    x_movement += abs(a[0]-b[0])
    y_movement += abs(a[1]-b[1])
    cv2.putText(frame,question,(50,100), font, 0.5,(0,0,0),1)
    cv2.putText(frame,"Exit : Press 'q'",(50,400), font, 0.5,(0,0,0),1)
    
    text = 'x_movement: ' + str(x_movement)
    if not gesture: cv2.putText(frame,text,(50,50), font, 0.8,(0,0,255),1)
    text = 'y_movement: ' + str(y_movement)
    if not gesture: cv2.putText(frame,text,(50,100), font, 0.8,(0,0,255),1)

    if x_movement > gesture_threshold:
        gesture = 'No'
    elif y_movement > gesture_threshold:
        gesture = 'Yes'
    else:
        gesture = "Unable to Process, Try again"
    
     # Log the interaction
    if gesture != prev_gesture:
        # Log the interaction
        #time.sleep(5000)
        #question = input("Ask a Question: ")
        log_file.write(f"Question: {question}\n")
        log_file.write(f"Response: {gesture}\n")
        log_file.write(f"Timestamp: {datetime.datetime.now()}\n\n")
        log_file.flush()
        prev_gesture = gesture
    if gesture and gesture_show > 0:
        cv2.putText(frame,'Gesture Detected: ' + gesture,(50,50), font, 0.5,(0,0,0),1)
        gesture_show -=1
    if gesture_show == 0:
        gesture = False
        x_movement = 0
        y_movement = 0
        gesture_show = 60 #number of frames a gesture is shown
        
    #print distance(get_coords(p0), get_coords(p1))
    p0 = p1

    cv2.imshow('image',frame)
    out.write(frame)
    key = cv2.waitKey(1)

# Exit if 'q' is pressed
    if key & 0xFF == ord('q'):
        break
log_file.close()
cv2.destroyAllWindows()
cap.release()

