import cv2
import uuid
import time
import os, os.path
from os import walk
directory = 'C:/Users/PCAero/Desktop/FacialRecognition/PersonImages'

def BeginCapture():
    
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    

    if os.path.exists(directory):
        pass
    else:
        os.mkdir(directory)

    while True: 
        ret,frame=cap.read()
        imgname = directory + '/PersonImages{}.jpg'.format(str(uuid.uuid1()))
        cv2.imwrite(imgname,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows

def getImageNames(numPics):
    filenames = next(walk(directory), (None, None, []))[2]
    list = []
    counter = 0
    for i in filenames:
        list.append(i)
        counter += 1
        if counter == numPics:
            break
    return list

def deleteTemp():
    filenames = next(walk(directory), (None, None, []))[2]
    for i in filenames:
        path = directory + '/' + i
        os.remove(path)

