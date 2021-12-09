import pyrebase

#import to download image
import os

config = { 
    "apiKey": "AIzaSyAxV8-iToKuLitUmG48EEkIddvq7iYrN2Y",
    "authDomain": "facial-recongition-38069.firebaseapp.com",
    "databaseURL": "https://facial-recongition-38069-default-rtdb.firebaseio.com",
    "projectId": "facial-recongition-38069",
    "storageBucket": "facial-recongition-38069.appspot.com",
    "messagingSenderId": "937313859878",
    "appId": "1:937313859878:web:25d017bad4c1df1255e9e7"

}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
my_image = "landscape.jpg"

#upload image
#storage.child(my_image).put(my_image)

#to download image from firebase
#storage.child(my_image).download(filename="testingland.jpg", path = os.path.basename(my_image))

#to get url of image
# auth = firebase.auth()
# email = "nancyhana@oakland.edu"
# password = "nancyhana"
# user = auth.sign_in_with_email_and_password(email, password)
# url = storage.child(my_image).get_url(user['idToken'])

# print (url)

