from user import User

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

if __name__ == '__main__':

    intro()
