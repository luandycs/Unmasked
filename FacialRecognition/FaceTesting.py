#Importing openCV
import cv2 as cv
import os
import numpy as np
#Utilizing opencv build in facial recognizer
#make list of people in images manually
DIR = r'C:/Users/PCAero/Desktop/FacialRecognition/users'
#Base folder
#DIR = r'C:/Users/PCAero/Desktop/FacialRecognition/TestingFaces'
#DIR = r'C:/Users/PCAero/Desktop/FacialRecognition/users'

#harr_face classifier 
haar_cascade = cv.CascadeClassifier('C:/Users/PCAero/Desktop/FacialRecognition/haar_face.xml')

#Create function that will loop over every folder and image and add them to the training set
#For every face there is a name


def create_train(people, DIR):
    features = []
    labels =[]
    #loop over every person in list
    for person in people:
        #grab path for each person file
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        #Loop over every image in file
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_RGB2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=16)
            
            #rectangle around face
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append (faces_roi)
                #index of list (mapping between string and numerical label, which lightens load on hardware)
                labels.append(label)
    features = np.array(features, dtype='object')
    labels = np.array(labels)
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(features,labels)
    face_recognizer.save('face_trained.yml')
    np.save('features.npy', features)
    np.save('labels.npy', labels)
                    


#Testing to see how many faces and labels we have
#print(f'Length of the features = {len(features)}')
#print(f'Length of the labels = {len(labels)}')

#Convert features and labels to numpy


#instantiate face recognizer


#train recognizer on features and labels list


#lets you save the model to use in another directory 




my_image = "landscape.jpg"


