class User: 
    '''
    class that generates new instances of users accounts
    '''
    user_list = []#user list
    def save_user(self):
        '''
        save_user method saves users
        '''
        User.user_list.append(self)
    def __init__(self,first_name,second_name,password):

       #create new user instance

        self.first_name = first_name
        self.second_name = second_name
        self.password = password
    
    @classmethod
    def display_users(cls):
        '''
        method to display all the users
        '''
        return cls.user_list