from user import User
import string
import random
import getpass
import pyperclip
from credentials import Credential

def create_credential(account_name,passkey):
    '''
    function to create a new credential
    '''
    new_credential = Credential(account_name,passkey)
    return new_credential
def save_credential(credential):
    '''
    function to save a credential
    '''
    credential.save_credential()
def display_credentials():
    '''
    function that dispalys all credentials
    '''
    return Credential.display_credentials()
def del_credential(credential):
    '''
    function to delete a credential
    '''
    credential.del_credential()
def check_existing_user(password2):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password2)
def find_account(password2):
    '''
    function to find account by its name
    '''
    return User.find_account(password2)


def create_user(f_name,s_name,password):
    '''
    function to create a new user
    '''
    new_user = User(f_name,s_name,password)
    return new_user
def save_users(user):
    '''
    function to save a user
    '''
    user.save_user()
def display_users():
    '''
    function that dispalys all signed up users
    '''
    return User.display_users()
def intro():
    print("Hey there! Welcome to Password Locker")
    print('\n')
    print("Please sign up for an account to enjoy services")
    
    while True:
        print("⇨ Use these short codes : su - Sign up, lg - login, du-display all users, ex-Exit app ")
        print('-'*64)
        print('\n')
        short_code = input().lower()
        print('\n')
        if short_code == 'su':
            print("New User")
            print("-"*9)

            print("Enter you first name...")
            f_name = input()

            print("Enter your second name...")
            s_name=input()

            print("Enter your password...")
            password=input()
            print('\n')

            save_users(create_user(f_name,s_name,password))
            print('\n')
            print(f"⇨ Congratulations {f_name} {s_name}, you now have an account \n")
            print('\n')

if __name__ == '__main__':

    intro()
