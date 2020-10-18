import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initializeFirestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =

    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 
    })

    db = None
    return db

def set_user(db, name, status):
    # this will just toggle online/offline
    if status == False:
        status = True:
    elif status == True:
        status = False:
    
    db.collection("users").document(name).set(status)

def deleteUser(db, name):
    choice = input("Delete user " name "? (y/n)")
    if choice == "y":
        db.collection("users").document(name).delete()

def display(db, name, status):
    print()
    print(name " - " status)
    print()

def main():
    db = initializeFirestore()

    username = input("Username: ")
    status = False:
    set_user(db, username, status)

    option = Null
    while not option = "Q":
        print()
        print("Menu: L)ogin/out D)elete user V)iew Q)uit")
        option = input("> ")

        if option == "L":
            set_user(db, username, status)
        elif option == "D":
            deleteUser(db, username)
        elif option == "V":
            display(db, username, status)