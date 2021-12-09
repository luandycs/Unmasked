import cv2
from firebase_admin import initialize_app
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('C:/Users/PCAero/Desktop/FacialRecognition/Cascades/data/haarcascade_frontalface_alt2.xml')
profile_cascade = cv2.CascadeClassifier('C:/Users/PCAero/Desktop/FacialRecognition/Cascades/data/haarcascade_profileface.xml')

class RectObject:
    def CreateRectangle(self,x1,y1,width,height, frame, color=(255,0,0)):
        self.x1 = x1
        self.y1=y1
        self.width=width
        self.height=height
        IsActive = True
        color=color
        stroke = 2
        end_cord_x= x1+width
        end_cord_y = y1+height
        #cv2.rectangle(frame,(x1,y1),(end_cord_x,end_cord_y), color, stroke)


def SaveImage(roi_gray):
    img_item = "my-image.png"
    cv2.imwrite(img_item,roi_gray)
    print("Image Saved")

def CloseCapture():
    print("capture")

def BeginTimer(t, r1, r2):
    cd = t 
    mins,secs = divmod(cd,60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    if mins < 10:
        mins = "0" + str(mins)
    else:
        mins = str(mins)
    if secs-1 < 10:
        secs = "0" + str(secs-1)
    else:
        secs = str(secs-1)
    if r1 != None:
        print("Reccording Will Begin In: " + mins + "m:"+secs+"s")
        time.sleep(1)
        return t-1
    elif r2 != None:
        print("Reccording Will Begin In: " + mins + "m:"+secs+"s")
        time.sleep(1)
        return t-1
    else:
        return 5

def ObjectInstance(Rectangle):
    result = isinstance(Rectangle,RectObject)
    if result:
        print("This Object Exists")
        return True
    else:
        return False


def capture():
    #load the first webcam, change the argument if you have multiple webcams
    cap = cv2.VideoCapture(0)
    TimeElapsed = False
    t = 5

    while True:
        try:
            #capture frame by frame
            ret, frame=cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            sideprof = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            R1 = None
            R2 = None
            cv2.imshow("Facial Detector", frame)
            #Rectangle
            for(x,y,w,h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                R1=RectObject()
                R1.CreateRectangle(x,y,w,h,frame)
            for(x,y,w,h) in sideprof:
                print(x,y,w,h)
                roi_gray2 = gray[y:y+h, x:x+w]
                roi_color2 = frame[y:y+h, x:x+w]
                R2=RectObject()
                R2.CreateRectangle(x,y,w,h,frame,(255,255,0))

            cd = BeginTimer(t, R1, R2)
            if cd == 0:
                TimeElapsed = True
            else:
                t = cd
            if TimeElapsed:
                SaveImage(frame)
                TimeElapsed = False
                t = 5
                break
        except KeyboardInterrupt:
            break
    
    cap.release()
    cv2.destroyAllWindows
