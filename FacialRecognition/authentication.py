import pyrebase

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
auth = firebase.auth()

#create user
email = "nancyhana@oakland.edu"
password = "nancyhana"

#uncomment when creating user and then comment when done 
#auth.create_user_with_email_and_password(email, password)

#sign in 
user = auth.sign_in_with_email_and_password(email, password)
#print(user)
#print(user ['idToken'])

#get account information 
#info = auth.get_account_info(user['idToken'])
#print(info)

#verify email 
#auth.send_email_verification(user['idToken'])

