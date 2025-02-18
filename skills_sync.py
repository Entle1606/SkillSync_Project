
import firebase_admin
from firebase_admin import credentials, firestore,auth

cred = credentials.Certificate(r"C:\Users\EMats\OneDrive\Documents\GitHub\SkillSync_Project\admin_sdk_demo\skillsync-project-1abfa-firebase-adminsdk-fbsvc-8bf59f1ac3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



def sign_up(email, password, role ="peer", name = "Default name"):
    
    if role not in ['mentor', 'peer']:
        print("Invalid role. Please choose either 'mentor' or 'peer'.")
        return
    try:
        user = auth.create_user(email=email, password =password)
        
        user_ref = db.collection("users").document(user.uid)
        user_ref = {
            "e-mail" : email,
            "role": role,
            "name": "default name" #to be updated
        }
        print(f'User created successfully! UID: {user.uid} and {role}')           
    except auth.InvalidEmailError:
         print(f"The email {email} is invalid. Please enter a valid email address.")
    except auth.WeakPasswordError:
        print("The password is too weak. Please choose a stronger password.")
    except Exception as e:
        print(f'Error creating user: {str(e)}')

def get_user_role(uid):
    while True:
        role = input("Please select your role (mentor/peer): ").lower().strip()
        if role in ['mentor', 'peer']:
            return role
        else:
            print("Invalid input. Please choose either 'mentor' or 'peer'.")



def test_create_user():
    try:
        user = auth.create_user(email='ematshikiza@gmail.com', password='testPassword123')
        print(f"User created successfully! UID: {user.uid}")
    except Exception as e:
        print(f"Error creating user: {str(e)}")

test_create_user()



# from pathlib import Path
# print("cWD")
# print( Path.cwd())

# if __name__ == "__main__":


    