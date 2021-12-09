from pyasn1.type.univ import Null
import pyrebase
# import to download image
import os
import firebase_admin
from firebase_admin import db
import json
from PIL import Image
#import FaceRecognition as FR

class FireBase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyAxV8-iToKuLitUmG48EEkIddvq7iYrN2Y",
            "authDomain": "facial-recongition-38069.firebaseapp.com",
            "databaseURL": "https://facial-recongition-38069-default-rtdb.firebaseio.com",
            "projectId": "facial-recongition-38069",
            "storageBucket": "facial-recongition-38069.appspot.com",
            "messagingSenderId": "937313859878",
            "appId": "1:937313859878:web:25d017bad4c1df1255e9e7"
        }
        self.cred_obj = firebase_admin.credentials.Certificate(
            'C:/Users/PCAero/Desktop/FacialRecognition/facial-recongition-38069-firebase-adminsdk.json')
        self.default_app = firebase_admin.initialize_app(
            self.cred_obj, {'databaseURL': self.config["databaseURL"]})

        self.database = pyrebase.initialize_app(self.config)
        self.storage = self.database.storage()
        self.auth = self.database.auth()
        self.path = "C:/Users/PCAero/Desktop/FacialRecognition/"

    #uploads image to firebase storage and updates path of picture1 field for the user
    #automatically increments the picture field and adds the picture
    #def addUserPic(self, userid, my_image):
    #    index = 0
    #    for i in range(len(my_image)-1, 0, -1):
    #        if my_image[i] in "/":
    #            index = i
    #            break
    #    name = my_image[i::]
    #
    #    if self.checkExistingPictureName(userid, name):
    #        print("Image already exists")
    #    else:
    #        self.storage.child(name).put(my_image)
    #       url = self.storage.child(name).path
    #        ref = db.reference('/users/'+userid)
    #
    #        pictureCounter = self.lastOccurence(userid) + 1
    #        pictureStr = "picture" + str(pictureCounter)
    #        ref.update({pictureStr: url})
    def addUserPic(self, userid, img):
        index = 0
        for i in range(len(img)-1, 0, -1):
            if img[i] in "/":
                index = i
                break
        pictureCounter = self.lastOccurence(userid) + 1
        pictureStr = "picture" + str(pictureCounter)
        name = pictureStr + userid + '_' + img[index+1::]

        self.storage.child(name).put(img)
        url = self.storage.child(name).path
        ref = db.reference('/users/'+userid)
        ref.update({pictureStr: url})

    def addOffendingPic(self, userid, img):
        index = 0
        for i in range(len(img)-1, 0, -1):
            if img[i] in "/":
                index = i
                break
        pictureCounter = self.lastOccurence(userid) + 1
        pictureStr = "offense" + str(pictureCounter)
        name = pictureStr + userid + '_' + img[index+1::]

        self.storage.child(name).put(img)
        url = self.storage.child(name).path
        ref = db.reference('/users/'+userid)
        ref.update({pictureStr: url})

    #checks if there is the same name of an image in a picture field
    def checkExistingPictureName(self, userid, name):
        ref = db.reference('/users/'+userid)
        temp = ref.get()
        pictureCounter = self.lastOccurence(userid)
        if pictureCounter == 0:
            return False
        else:
            for i in range(pictureCounter+1, 1, 1):
                pictureStr = "picture" + str(i)
                ref = db.reference('/users/'+userid+'/'+pictureStr)
                temp = ref.get()
                print(temp)

    #creates or updates userid with data
    def createUser(self, userid, data):
        ref = db.reference('/users/'+userid)
        ref.update(data)
    
    #changes specific fields for a user
    def changeUserData(self, userid, data):
        ref = db.reference('/users/'+userid)
        old_data = ref.get()
        if data is not Null:
            for key, value in data.items():
                ref.update({key: value})


    # deletes a field of a user
    def deleteField(self, userid, field):
        ref = db.reference('/users/'+userid+'/'+field)
        ref.delete()

    # deletes user
    def deleteUser(self, userid):
        ref = db.reference('/users/'+userid)
        ref.delete()
 
    #downloads user pictures of userid and returns a list of file names
    def getUserPictures(self, userid):
        ref = db.reference('/users/'+userid)
        index = self.lastOccurence(userid)
        temp = []
        values = ref.get()
        fName = values["f_name"]
        lName = values["l_name"]
        for i in range (1, index+1):
            field = "picture"+str(i)
            temp.append(values[field])
        
        path = self.path + 'users/'
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
        path = path + fName + ' ' + lName +'/'
        self.downloadPictures(temp, path)
        return temp

    #downloads all images in list
    def downloadPictures(self, list, path):
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            
        for i in list:          
            if os.path.exists(path+i):
                #print(i + " already exists.")
                pass
            else:
                print("Downloading: "+i)
                self.storage.child(i).download(filename=path+i, path=path)

    #returns all Grizzly IDs of users
    def getAllUserID(self):
        ref = db.reference('/users/')
        users = ref.get()
        return users

    #returns all Grizzly student names
    def getAllNames(self):
        temp = self.getAllUserID()
        users = []
        for i in temp:
            ref = db.reference('/users/'+i)
            ref = ref.get()
            fName = ref["f_name"]
            lName = ref["l_name"]
            name = fName + " " + lName
            users.append(name)
        return users
    
    def getEmail(self, userid):
        ref = db.reference('/users/'+userid)
        values = ref.get()
        email = values["email"]
        return email

    def getLastOffense(self, userid):
        offenseCounter = self.lastOffenseOccurence(userid)
        ref = db.reference('/users/' + userid + '/offense' + offenseCounter)
        ref = ref.get()
        im = Image.open(ref)
        return im



    #retrieves the entire database of users and their pictures
    def getAllPictures(self):
        users = self.getAllUserID()
        for i in users:
            self.getUserPictures(i)
               
    def getPath(self):
        return self.path

    def getUserID(self, name):
        temp = self.getAllUserID()
        for i in temp:
            ref = db.reference('/users/' + i)
            ref = ref.get()
            fName = ref["f_name"]
            lName = ref["l_name"]
            fullName = fName + " " + lName
            if name == fullName:
                return i
        return None

    # finds the how many pictures there are and returns the count
    def lastOccurence(self, userid):
        ref = db.reference('/users/'+userid)
        temp = ref.get()
        temp = json.dumps(temp)
        index = temp.rfind('picture')
        index = index+7

        count = ""
        for i in temp[index]:
            if i.isnumeric():
                count = count + i

        if count == "":
            return 0
        else:
            return int(count)

    def lastOffenseOccurence(self, userid):
        ref = db.reference('/users/'+userid)
        temp = ref.get()
        temp = json.dumps(temp)
        index = temp.rfind('offense')
        index = index+7

        count = ""
        for i in temp[index]:
            if i.isnumeric():
                count = count + i

        if count == "":
            return 0
        else:
            return int(count)
    
    def iterateOffenses(self, userid):
        ref = db.reference('/users/' + userid + '/offenses')
        offenses = ref.get()
        if offenses == None:
            data = {"offenses": "1"}
            self.changeUserData(userid, data)
        else:
            offenses = int(offenses)
            offenses += 1
            data = {"offenses": offenses}
            self.changeUserData(userid, data)
    
    def resetOffenses(self, userid):
        data = {"offenses": "0"}
        self.changeUserData(userid, data)

