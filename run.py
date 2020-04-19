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
        elif short_code == 'lg':

            print("Enter the first name of your registered account")
            account_name = input()
            print('\n')

            authentification = getpass.getpass('Password:')
            if check_existing_user(authentification):
                search_account = find_account(authentification)



                while True:
                    print(f"⇨ Welcome {search_account.first_name} {search_account.second_name} \n")
                    print("⇨ cc-To create new credential, vc-To view all your credentials, ex-exit account \n ")
                    print('-'*80)
                    short_code=input().lower()
                    if short_code == 'cc':
                        print("New credential")
                        print('-'*14)
                        print("Enter account name")
                        account_name = input()
                        print("Make a password \n")
                        print("To make your own password press- a, to generate a password press - g \n")
                        print('-'*50)
                        generate=input()
                        print('\n')

                        if generate == 'g':
                            letters = string.ascii_letters + string.digits
                            gpassword = ''.join(random.choice(letters) for i in range(9))
                            print(f"Your new generated password is: {gpassword} \n")
                            passkey=gpassword

                        elif generate == 'a':
                            print("Enter its password")
                            passkey = input()
                            print('\n')
                        print(f"👍_{account_name} has been saved")

                        save_credential(create_credential(account_name,passkey))

                    elif short_code == 'vc':
                        if display_credentials:
                            print("⇨ Here is a list of all your accounts and passwords \n")
                            for credential in display_credentials():
                                print(f"Account name: {credential.account_name} - password: {credential.passkey}")
                    elif short_code == 'dc':
                        print("Which credential would you like to delete?")
                        del_account = input()
                        if del_account == account_name:

                            Credential.credential_list.remove(credential)
                            print("👍_Credential deleted")
                        else:
                            print("No match of such a credential")

                    elif short_code == 'ex':
                        print("You have exited your account \n")
                        break
            else:
                print("The password was incorrect \n")
                print('\n')
         elif short_code == 'du':
            print("Here is a list of all the users\n")
            for user in display_users():
                print(f"{user.first_name} {user.second_name} \n")



if __name__ == '__main__':

    intro()
